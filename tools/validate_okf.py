#!/usr/bin/env python3
"""Validate OKF bundles: frontmatter, required `type`, link resolution, Sources.

Concept files under a bundle root get the full checks. Auxiliary files that
reference the bundles (README.md, .claude/skills/**/*.md) get a lighter
reference check: every local markdown-link target and repo-path code span must
resolve. With no arguments the whole repo is checked (bundles + aux files);
with explicit path arguments only those paths are checked as bundle roots.
"""
import re, sys, pathlib

try:
    import yaml
except ModuleNotFoundError:
    sys.exit(
        "validate_okf.py needs PyYAML to parse frontmatter the way GitHub does.\n"
        "Run `uv sync` once, then invoke via `uv run tools/validate_okf.py`."
    )

REPO = pathlib.Path(__file__).resolve().parent.parent
FM = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
LINK = re.compile(r"\]\((/[^)]+\.md)\)")
# Auxiliary references. Markdown links are matched OUTSIDE inline-code spans
# (so documentation that shows link *syntax* in backticks isn't treated as a
# real link); repo-path examples are matched INSIDE backticks and must start
# with a real top-level dir (so syntax illustrations like `](/....md)` don't
# match).
CODE_SPAN = re.compile(r"`[^`]*`")
MD_LINK = re.compile(r"\]\(([^)]+)\)")
CODE_PATH = re.compile(r"`(/?(?:oks|docs|tools|\.claude)/[^`]+\.md)`")

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
            else:
                # Strict-parse with PyYAML: GitHub rejects frontmatter a regex
                # check tolerates (e.g. an unquoted `: ` inside a description).
                try:
                    fm = yaml.safe_load(m.group(1))
                except yaml.YAMLError as e:
                    mark = getattr(e, "problem_mark", None)
                    where = f" at line {mark.line + 1} column {mark.column + 1}" if mark else ""
                    problem = getattr(e, "problem", None) or e
                    errors.append(f"{rel}: invalid YAML frontmatter{where}: {problem}")
                else:
                    if not isinstance(fm, dict):
                        errors.append(f"{rel}: frontmatter is not a YAML mapping")
                    elif not str(fm.get("type") or "").strip():
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
    refs = MD_LINK.findall(CODE_SPAN.sub("", text)) + CODE_PATH.findall(text)
    for raw in refs:
        ref = raw.split()[0].split("#")[0]  # strip title/fragment
        if not ref or ref.startswith(("http://", "https://", "mailto:")):
            continue
        base = REPO if ref.startswith("/") else path.parent
        if not (base / ref.lstrip("/")).exists():
            errors.append(f"{rel}: broken reference -> {ref}")
    return errors

def aux_files():
    files = []
    for name in ("README.md", "CLAUDE.md"):
        f = REPO / name
        if f.exists():
            files.append(f)
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
