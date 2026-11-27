#!/usr/bin/env python3
"""Install the software factory into a product repository.

    python scripts/install.py <path-to-product-repo> [--dry-run]

Copies assets/repo-template/ (factory/, tasks/, retros/, .github/ files, .prettierignore)
into the repository root. It never overwrites: a repo that already has factory/ is left
alone, and an existing CODEOWNERS or .prettierignore gets the factory's lines appended.
It does not commit, push or change branch protection; it prints what is left to do.

Standard library only. `factoryctl` itself needs PyYAML.
"""
import argparse
import os
import shutil
import subprocess
import sys

TEMPLATE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "assets", "repo-template")
COPY_DIRS = ["factory", "tasks", "retros"]
COPY_FILES = [".github/workflows/factory-guard.yml"]
APPEND_FILES = [".github/CODEOWNERS", ".prettierignore"]      # merged line by line if they exist
SKIP = shutil.ignore_patterns("__pycache__", "*.pyc")


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("repo", help="root of the product repository")
    ap.add_argument("--dry-run", action="store_true", help="show what would be written, write nothing")
    a = ap.parse_args()
    repo = os.path.abspath(a.repo)

    if not os.path.exists(os.path.join(repo, ".git")):
        sys.exit(f"install: {repo} is not the root of a git repository")
    if os.path.exists(os.path.join(repo, "factory")):
        sys.exit(f"install: {repo}/factory already exists. The factory is installed (or the name is taken). "
                 "Change an installed factory through a factory_change task, not by reinstalling.")

    done = []
    for d in COPY_DIRS:
        src, dst = os.path.join(TEMPLATE, d), os.path.join(repo, d)
        if os.path.exists(dst):
            done.append(f"kept      {d}/ (already there)")
            continue
        if not a.dry_run:
            shutil.copytree(src, dst, ignore=SKIP)
        done.append(f"copied    {d}/")
    for f in COPY_FILES:
        src, dst = os.path.join(TEMPLATE, f), os.path.join(repo, f)
        if os.path.exists(dst):
            sys.exit(f"install: {f} already exists and is not the factory's. Resolve by hand.")
        if not a.dry_run:
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            shutil.copyfile(src, dst)
        done.append(f"copied    {f}")
    for f in APPEND_FILES:
        src, dst = os.path.join(TEMPLATE, f), os.path.join(repo, f)
        with open(src, encoding="utf-8") as fh:
            ours = fh.read()
        if not os.path.exists(dst):
            if not a.dry_run:
                os.makedirs(os.path.dirname(dst) or repo, exist_ok=True)
                with open(dst, "w", encoding="utf-8", newline="\n") as fh:
                    fh.write(ours)
            done.append(f"copied    {f}")
            continue
        with open(dst, encoding="utf-8") as fh:
            theirs = fh.read()
        missing = [l for l in ours.splitlines() if l.strip() and not l.startswith("#") and l not in theirs.splitlines()]
        if missing and not a.dry_run:
            with open(dst, "a", encoding="utf-8", newline="\n") as fh:
                fh.write(("" if theirs.endswith("\n") else "\n") + "\n# software factory\n" + "\n".join(missing) + "\n")
        done.append(f"appended  {f} (+{len(missing)} line(s))" if missing else f"kept      {f}")

    print(("DRY RUN — nothing written\n" if a.dry_run else "") + "\n".join(done))
    if a.dry_run:
        return

    check = subprocess.run([sys.executable, os.path.join(repo, "factory", "bin", "factoryctl"), "check"],
                           capture_output=True, text=True, encoding="utf-8", errors="replace")
    if check.returncode == 0:
        print("\nfactoryctl check: " + check.stdout.strip())
    elif "No module named 'yaml'" in check.stderr:
        print("\nfactoryctl check: not run — this Python has no PyYAML. Run it with one that does.")
    else:
        sys.exit("\nfactoryctl check FAILED:\n" + check.stderr)

    print("""
Left to do (a human decides these):
  1. .github/CODEOWNERS: replace @your-org/factory-owners with a real team.
  2. factory/factory.yaml: adapt classification.path_triggers, size_thresholds and controls to this repo.
  3. AGENTS.md / CLAUDE.md: add the short "Software Factory" section from the skill's Install
     steps, so later agents know the factory is here and use the skill.
  4. Commit on a branch and merge by hand, e.g. "factory init v4.0".
  5. Protect main: require PRs, the `factory-guard` check, the product's tests and code-owner
     review; forbid force-push.""")


if __name__ == "__main__":
    main()
