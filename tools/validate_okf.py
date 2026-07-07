#!/usr/bin/env python3
"""Validate OKF bundles: frontmatter, required `type`, link resolution, Sources.

Concept files under a bundle root get the full checks. Auxiliary files that
reference the bundles (README.md, .claude/skills/**/*.md) get a lighter
reference check: every local markdown-link target and repo-path code span must
resolve. With no arguments the whole repo is checked (bundles + aux files);
with explicit path arguments only those paths are checked as bundle roots.
"""
import re, sys, pathlib

REPO = pathlib.Path(__file__).resolve().parent.parent
FM = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
LINK = re.compile(r"\]\((/[^)]+\.md)\)")
# Auxiliary references: markdown-link targets, or repo-path code spans ending .md
AUX_REF = re.compile(r"\]\(([^)]+)\)|`(/?(?:oks|docs|tools|\.claude)/[^`]+\.md)`")

def concepts(root):
    return [p for p in root.rglob("*.md")]

def display(p):
    try:
        return p.relative_to(REPO)
    except ValueError:
        return p

def check(root):
    errors = []
    for p in concepts(root):
        text = p.read_text(encoding="utf-8")
        rel = display(p)
        name = p.name
        m = FM.match(text)
        if name != "log.md":
            if not m:
                errors.append(f"{rel}: missing YAML frontmatter")
            elif not re.search(r"^type:\s*\S", m.group(1), re.MULTILINE):
                errors.append(f"{rel}: frontmatter missing required `type`")
        if name not in ("index.md", "log.md") and "# Sources" not in text:
            errors.append(f"{rel}: missing `# Sources` section")
        for target in LINK.findall(text):
            if not (REPO / target.lstrip("/")).exists():
                errors.append(f"{rel}: broken link -> {target}")
    return errors

def check_aux(path):
    """Reference-only check for files that point at the bundles."""
    errors = []
    if not path.exists():
        return errors
    text = path.read_text(encoding="utf-8")
    rel = display(path)
    for mdlink, codepath in AUX_REF.findall(text):
        ref = (mdlink or codepath).split()[0].split("#")[0]  # strip title/fragment
        if not ref or ref.startswith(("http://", "https://", "mailto:")):
            continue
        base = REPO if ref.startswith("/") else path.parent
        if not (base / ref.lstrip("/")).exists():
            errors.append(f"{rel}: broken reference -> {ref}")
    return errors

def aux_files():
    files = []
    readme = REPO / "README.md"
    if readme.exists():
        files.append(readme)
    skills = REPO / ".claude" / "skills"
    if skills.exists():
        files += sorted(skills.rglob("*.md"))
    return files

def main():
    args = sys.argv[1:]
    errors = []
    if args:
        for a in args:
            r = pathlib.Path(a).resolve()
            if r.exists():
                errors += check(r)
    else:
        errors += check(REPO / "oks")
        for aux in aux_files():
            errors += check_aux(aux)
    for e in errors:
        print(e)
    print(f"\n{len(errors)} violation(s)")
    sys.exit(1 if errors else 0)

if __name__ == "__main__":
    main()
