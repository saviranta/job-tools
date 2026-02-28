#!/usr/bin/env python3
"""
eval.py — Mechanical eval checks for a generated CV/CL application.

Runs three checks against the markdown output files:
  1. Keyword coverage   — are job-brief keywords present in the CV and CL?
  2. Citation integrity — do source comments trace back to real capability entries?
  3. Metric integrity   — do all metrics in the CV appear verbatim in the assets?

Usage:
    python eval.py <application_folder> [assets_folder]

    application_folder  Path to applications/company-role-date/
    assets_folder       Path to assets/ folder
                        (default: inferred as ../../assets from application_folder)

Examples:
    python eval.py ~/cv-workspace/applications/acme-pm-20260228
    python eval.py ~/cv-workspace/applications/acme-pm-20260228 ~/cv-workspace/assets
"""

from __future__ import annotations

import sys
import re
from pathlib import Path


# ─── File helpers ──────────────────────────────────────────────────────────────

def find_md(folder: Path, tag: str) -> Path | None:
    """Find a file matching *_<tag>.md in folder. Returns most recent if multiple."""
    matches = sorted(folder.glob(f"*_{tag}.md"))
    return matches[-1] if matches else None


def read(path: Path | None) -> str:
    if path is None or not path.exists():
        return ""
    return path.read_text(encoding="utf-8")


# ─── Parsers ───────────────────────────────────────────────────────────────────

def parse_keywords(job_brief: str) -> list[str]:
    """
    Extract keyword phrases from section 6 of job-brief.md.
    Expects the section header to contain "Keywords" and items as bullet points.
    """
    # Find section 6 — everything between **6. Keywords...** and **7.**
    section_match = re.search(
        r'\*\*6\.\s*Keywords[^\*]*?\*\*(.*?)(?=\*\*7\.|\Z)',
        job_brief,
        re.DOTALL | re.IGNORECASE,
    )
    if not section_match:
        return []

    section = section_match.group(1)
    keywords = []

    for line in section.split("\n"):
        # Match bullet lines: "- keyword" or "- "keyword"" or "- **keyword**"
        m = re.match(r'^\s*-\s+["`*]{0,2}(.+?)["`*]{0,2}\s*$', line)
        if not m:
            continue
        kw = m.group(1).strip().strip('"').strip("'")
        # Skip category sub-headers: italic like *Role-specific terms* or
        # lines containing "terms", "words", "phrases" (heading-like phrases)
        if re.match(r'^\*[^*]+\*$', kw):
            continue
        if re.search(r'\b(?:terms|words|phrases|skills|competencies)\b', kw, re.I):
            continue
        # Skip if too long to be a phrase (likely a description)
        if 2 < len(kw) < 60:
            keywords.append(kw.lower())

    return keywords


def parse_source_citations(cv_md: str) -> list[str]:
    """Extract entry titles from <!-- source: X --> comments in CV markdown."""
    return re.findall(r'<!--\s*source:\s*(.+?)\s*-->', cv_md)


def get_entries_section(capabilities_md: str) -> str:
    """Return only the ## ENTRIES section from capabilities.md."""
    m = re.search(
        r'^## ENTRIES\s*\n(.*?)(?=^## |\Z)',
        capabilities_md,
        re.DOTALL | re.MULTILINE,
    )
    return m.group(1) if m else capabilities_md  # fallback: use full file


def parse_entry_titles(capabilities_md: str) -> dict[str, str]:
    """
    Return {title_lowercase: full_entry_text} from ENTRIES section.
    Matches headers like: ### CAP-001 — Entry title [ROLE-001]
    """
    entries_text = get_entries_section(capabilities_md)
    title_pattern = re.compile(
        r'^### (?:CAP-\d+)\s+[—-]\s+(.+?)(?:\s+\[[A-Z0-9\-]+\])?\s*$',
        re.MULTILINE,
    )
    matches = list(title_pattern.finditer(entries_text))
    result = {}
    for i, m in enumerate(matches):
        title = m.group(1).strip()
        start = m.start()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(entries_text)
        result[title.lower()] = entries_text[start:end]
    return result


# Metric patterns that are worth checking (numbers likely to be hallucinated)
_METRIC_PATTERNS = [
    r'\b~?\d+(?:\.\d+)?\s*%',                         # 40%, ~2.5%
    r'\b~?\d+(?:\.\d+)?[xX×]\b',                      # 3x, ~2X
    r'[$€£]\s*~?\d+(?:[.,]\d+)?\s*[kKmMbBtT]?\b',    # $2M, €500k
    r'\b~?\d+(?:[.,]\d+)?\s*[kK]\b',                  # 50k (standalone)
    r'\b~?\d+(?:[.,]\d+)?\s*(?:million|billion|thousand)\b',  # spelled-out
    r'\b~?\d{1,3}(?:,\d{3})+\b',                      # 1,000 / 10,000
]


def extract_metrics(cv_md: str) -> list[str]:
    """
    Find metric-like tokens from bullet point lines in cv markdown.
    Only looks in bullet lines to reduce false positives from dates, IDs, etc.
    """
    bullet_lines = [l for l in cv_md.split("\n") if re.match(r'\s*[-•*]\s', l)]
    content = "\n".join(bullet_lines)

    found = []
    seen: set[str] = set()
    for pattern in _METRIC_PATTERNS:
        for m in re.finditer(pattern, content, re.IGNORECASE):
            token = m.group(0).strip()
            # Exclude 4-digit years
            if re.match(r'^(?:19|20)\d{2}$', token):
                continue
            if token not in seen:
                seen.add(token)
                found.append(token)
    return found


# ─── Checks ────────────────────────────────────────────────────────────────────

def check_keyword_coverage(job_brief: str, cv: str, cl: str) -> dict:
    keywords = parse_keywords(job_brief)
    if not keywords:
        return {
            "skipped": True,
            "reason": "Section 6 not found or empty in job-brief.md",
        }
    combined = (cv + " " + cl).lower()
    hits, misses = [], []
    for kw in keywords:
        if kw in combined:
            hits.append(kw)
        else:
            misses.append(kw)
    return {
        "skipped": False,
        "total": len(keywords),
        "hits": hits,
        "misses": misses,
        "pass": len(misses) == 0,
    }


def check_citation_integrity(cv: str, capabilities: str) -> dict:
    citations = parse_source_citations(cv)
    if not citations:
        return {
            "skipped": False,
            "warning": (
                "No <!-- source: X --> citations found in CV markdown. "
                "Were source comments added during Phase 2?"
            ),
            "pass": False,
        }
    if not capabilities:
        return {
            "skipped": True,
            "reason": "capabilities.md not found — cannot verify citations",
        }
    entry_map = parse_entry_titles(capabilities)
    verified, unverified = [], []
    for cite in citations:
        if cite.strip().lower() in entry_map:
            verified.append(cite)
        else:
            unverified.append(cite)
    return {
        "skipped": False,
        "total": len(citations),
        "verified": verified,
        "unverified": unverified,
        "pass": len(unverified) == 0,
    }


def check_metric_integrity(cv: str, capabilities: str) -> dict:
    metrics = extract_metrics(cv)
    if not metrics:
        return {
            "skipped": True,
            "reason": "No metric patterns found in CV bullet lines",
        }
    if not capabilities:
        return {
            "skipped": True,
            "reason": "capabilities.md not found — cannot verify metrics",
        }
    entries_text = get_entries_section(capabilities)
    verified, unverified = [], []
    for m in metrics:
        if m.lower() in entries_text.lower():
            verified.append(m)
        else:
            unverified.append(m)
    return {
        "skipped": False,
        "total": len(metrics),
        "verified": verified,
        "unverified": unverified,
        "pass": len(unverified) == 0,
    }


# ─── Output helpers ────────────────────────────────────────────────────────────

def sym(passed: bool, skipped: bool = False) -> str:
    if skipped:
        return "—"
    return "✓" if passed else "✗"


def print_check(label: str, result: dict) -> None:
    skipped = result.get("skipped", False)
    s = sym(result.get("pass", False), skipped)

    if skipped:
        print(f"  {label:<26} {s}  ({result['reason']})")
    elif "warning" in result:
        print(f"  {label:<26} {s}  ⚠  {result['warning']}")
    elif "hits" in result:
        print(f"  {label:<26} {s}  {result['total'] - len(result['misses'])}/{result['total']} keywords present")
    elif "verified" in result:
        print(f"  {label:<26} {s}  {len(result['verified'])}/{result['total']} verified")


def print_details(kw: dict, cit: dict, met: dict) -> None:
    printed = False

    if not kw.get("skipped") and kw.get("misses"):
        print("  Missing keywords (not found in CV or CL text):")
        for m in kw["misses"]:
            print(f"    ✗  \"{m}\"")
        printed = True

    if "warning" in cit:
        pass  # already shown inline
    elif not cit.get("skipped") and cit.get("unverified"):
        if printed:
            print()
        print("  Unverified citations (entry title not found in capabilities.md):")
        for c in cit["unverified"]:
            print(f"    ✗  \"{c}\"")
        printed = True

    if not met.get("skipped") and met.get("unverified"):
        if printed:
            print()
        print("  Metrics not found in asset entries — hallucination risk:")
        for m in met["unverified"]:
            print(f"    ✗  {m}")
        printed = True

    if printed:
        print()


# ─── Main ──────────────────────────────────────────────────────────────────────

def main() -> None:
    if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
        print(__doc__)
        sys.exit(0 if sys.argv[1:] else 1)

    app_folder = Path(sys.argv[1]).expanduser().resolve()
    if not app_folder.is_dir():
        print(f"Error: folder not found: {app_folder}")
        sys.exit(1)

    # Infer assets folder: workspace/applications/name/ → workspace/assets/
    if len(sys.argv) >= 3:
        assets_folder = Path(sys.argv[2]).expanduser().resolve()
    else:
        assets_folder = app_folder.parent.parent / "assets"

    # Locate files
    cv_path           = find_md(app_folder, "cv")
    cl_path           = find_md(app_folder, "cl")
    job_brief_path    = app_folder / "job-brief.md"
    capabilities_path = assets_folder / "capabilities.md"

    # ── Header
    print()
    print("═" * 56)
    print(f"  EVAL — {app_folder.name}")
    print("═" * 56)
    print()

    # ── File status
    files_ok = True
    for label, path, required in [
        ("CV draft (.md)",     cv_path,           True),
        ("CL draft (.md)",     cl_path,           True),
        ("job-brief.md",       job_brief_path,    True),
        ("capabilities.md",    capabilities_path, False),
    ]:
        exists = path is not None and Path(path).exists()
        status = "✓" if exists else ("✗  MISSING" if required else "—  not found (skipping metric/citation checks)")
        print(f"  {label:<26} {status}")
        if required and not exists:
            files_ok = False

    if not files_ok:
        print()
        print("  Cannot run checks — required files missing.")
        print("═" * 56)
        sys.exit(1)

    print()

    # ── Load content
    cv           = read(cv_path)
    cl           = read(cl_path)
    job_brief    = read(job_brief_path)
    capabilities = read(capabilities_path)

    # ── Run checks
    kw  = check_keyword_coverage(job_brief, cv, cl)
    cit = check_citation_integrity(cv, capabilities)
    met = check_metric_integrity(cv, capabilities)

    # ── Print results
    print_check("Keyword coverage",      kw)
    print_check("Source citation check", cit)
    print_check("Metric integrity",      met)
    print()

    # ── Details for failures
    print_details(kw, cit, met)

    # ── Summary line
    issues = []
    if not kw.get("skipped") and kw.get("misses"):
        n = len(kw["misses"])
        issues.append(f"{n} missing keyword{'s' if n > 1 else ''}")
    if "warning" in cit:
        issues.append("source citations absent from CV")
    elif not cit.get("skipped") and cit.get("unverified"):
        n = len(cit["unverified"])
        issues.append(f"{n} unverified citation{'s' if n > 1 else ''}")
    if not met.get("skipped") and met.get("unverified"):
        n = len(met["unverified"])
        issues.append(f"{n} metric{'s' if n > 1 else ''} not in assets (hallucination risk)")

    if issues:
        print(f"  Issues: {' | '.join(issues)}")
    else:
        print("  All checks passed.")
    print("═" * 56)
    print()


if __name__ == "__main__":
    main()
