#!/usr/bin/env python3
"""Validate OKF bundles: frontmatter, required `type`, link resolution, Sources."""
import re, sys, pathlib

REPO = pathlib.Path(__file__).resolve().parent.parent
FM = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
LINK = re.compile(r"\]\((/[^)]+\.md)\)")

def concepts(root):
    return [p for p in root.rglob("*.md")]

def check(root):
    errors = []
    for p in concepts(root):
        text = p.read_text(encoding="utf-8")
        rel = p.relative_to(REPO)
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

def main():
    roots = [pathlib.Path(a) for a in sys.argv[1:]] or [REPO / "oks"]
    errors = []
    for r in roots:
        if r.exists():
            errors += check(r)
    for e in errors:
        print(e)
    print(f"\n{len(errors)} violation(s)")
    sys.exit(1 if errors else 0)

if __name__ == "__main__":
    main()
