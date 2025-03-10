# /// script
# requires-python = ">=3.12"
# dependencies = [
#   "pyyaml>=6.0.2",
# ]
# ///

"""
This script gathers all of the files needed to build the publication.
These files do not all exist in any single commit in the repository,
because the publication needs to include versions of the `index.ipynb` notebook
for each git tag.

This script executes the following steps:
- Copies the `index.ipynb` notebook from each tag to a `_freeze/index_v{tag}.ipynb` file.
- Copies the `_freeze/index` directory from each tag to a `_freeze/index_v{tag}` directory.
- Updates the `_quarto.yml` file to include a `version-control` item for each tag.
"""

import argparse
import os
import shutil
import subprocess
from contextlib import contextmanager
from pathlib import Path

import yaml


def get_versioned_notebook_path(tag: str) -> str:
    """Get the path to the `index.ipynb` notebook for a given tag."""
    return f"index_{tag}.ipynb"


def get_versioned_freeze_directory_path(tag: str) -> str:
    """Get the path to the `_freeze/index` directory for a given tag."""
    return f"_freeze/index_{tag}"


@contextmanager
def git_checkout(ref: str):
    original_ref = (
        subprocess.check_output(["git", "rev-parse", "--abbrev-ref", "HEAD"])
        .decode("utf-8")
        .strip()
    )

    try:
        subprocess.run(["git", "checkout", ref], check=True)
        yield
    finally:
        subprocess.run(["git", "checkout", original_ref], check=True)


def get_tags() -> list[str]:
    """Get a list of all git tags."""
    result = subprocess.run(["git", "tag"], capture_output=True, text=True, check=True)
    return result.stdout.splitlines()


def copy_notebook(tag: str, dry_run: bool) -> None:
    """Copy the `index.ipynb` notebook from a tagged release."""
    src = "index.ipynb"
    dst = get_versioned_notebook_path(tag)

    if dry_run:
        print(f"Would copy '{src}' to '{dst}'")
        return

    shutil.copy2(src, dst)


def copy_freeze_directory(tag: str, dry_run: bool) -> None:
    """Copy the `_freeze` directory from a tagged release."""
    src = "_freeze/index"
    dst = get_versioned_freeze_directory_path(tag)

    if dry_run:
        print(f"Would copy '{src}' to '{dst}'")
        return

    shutil.rmtree(dst, ignore_errors=True)
    shutil.copytree(src, dst)


def update_index_notebook(tag: str, dry_run: bool) -> None:
    """Rename the most recent tagged version of the notebook to `index.ipynb`."""
    notebook_src = get_versioned_notebook_path(tag)
    notebook_dst = "index.ipynb"

    freeze_src = get_versioned_freeze_directory_path(tag)
    freeze_dst = "_freeze/index"

    if dry_run:
        print(f"Would move '{notebook_src}' to '{notebook_dst}'")
        print(f"Would move '{freeze_src}' to '{freeze_dst}'")
        return

    os.remove(notebook_dst)
    shutil.rmtree(freeze_dst, ignore_errors=True)

    shutil.move(notebook_src, notebook_dst)
    shutil.move(freeze_src, freeze_dst)


def update_quarto_yaml(most_recent_tag: str, previous_tags: list[str], dry_run: bool) -> None:
    """Update the _quarto.yml file to include menu items for each tagged release."""
    yaml_path = Path("_quarto.yml")
    content = yaml.safe_load(yaml_path.read_text())

    most_recent_version_item = {
        "text": f"{most_recent_tag} (latest)",
        # The link for the most recent version is always `index.ipynb`.
        # (This version of the notebook is renamed to `index.ipynb` elsewhere in this script.)
        "href": "index.ipynb",
    }
    previous_version_items = [
        {"text": tag, "href": get_versioned_notebook_path(tag)} for tag in previous_tags
    ]

    if dry_run:
        print(f"Would update '{yaml_path}' with the following menu items:")
        print(f"  - {most_recent_version_item}")
        for item in previous_version_items:
            print(f"  - {item}")
        return

    # Insert the new items.
    for item in content["website"]["navbar"]["left"]:
        if "version-control" in item.get("text", ""):
            item["menu"] = [most_recent_version_item] + previous_version_items

    yaml_path.write_text(yaml.dump(content, sort_keys=False, allow_unicode=True))


def main() -> None:
    args = argparse.ArgumentParser()
    args.add_argument("--dry-run", action="store_true")
    args = args.parse_args()

    tags = get_tags()
    if not tags:
        raise ValueError("No tags found")

    for tag in tags:
        print(f"Processing tag {tag}")
        with git_checkout(tag):
            copy_notebook(tag, dry_run=args.dry_run)
            copy_freeze_directory(tag, dry_run=args.dry_run)

    tags = sorted(tags, reverse=True)
    most_recent_tag, *previous_tags = tags

    update_index_notebook(most_recent_tag, dry_run=args.dry_run)
    update_quarto_yaml(most_recent_tag, previous_tags, dry_run=args.dry_run)


if __name__ == "__main__":
    main()
