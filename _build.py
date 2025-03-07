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
from pathlib import Path

import yaml


def get_tags() -> list[str]:
    """Get a list of all git tags."""
    result = subprocess.run(["git", "tag"], capture_output=True, text=True, check=True)
    return result.stdout.splitlines()


def checkout_ref(ref: str) -> None:
    """Checkout the specified git ref."""
    subprocess.run(["git", "checkout", ref], check=True)


def copy_notebook(tag: str, dry_run: bool) -> None:
    """Copy the `index.ipynb` notebook from a tagged release."""
    src = "index.ipynb"
    dst = f"index_{tag}.ipynb"

    if dry_run:
        print(f"Would copy '{src}' to '{dst}'")
        return

    if os.path.exists(dst):
        shutil.rmtree(dst)
    shutil.copy2(src, dst)


def copy_freeze_directory(tag: str, dry_run: bool) -> None:
    """Copy the `_freeze` directory from a tagged release."""
    src = "_freeze/index"
    dst = f"_freeze/index_{tag}"

    if dry_run:
        print(f"Would copy '{src}' to '{dst}'")
        return

    if os.path.exists(dst):
        shutil.rmtree(dst)
    shutil.copytree(src, dst)


def update_quarto_yaml(tags: list[str], dry_run: bool) -> None:
    """Update the _quarto.yml file to include menu items for each tagged release."""
    yaml_path = Path("_quarto.yml")
    content = yaml.safe_load(yaml_path.read_text())

    tags = sorted(tags, reverse=True)
    most_recent_tag, *previous_tags = tags
    most_recent_version_item = {
        "text": f"{most_recent_tag} (latest)",
        "href": f"index_{most_recent_tag}.ipynb",
    }
    previous_version_items = [{"text": tag, "href": f"index_{tag}.ipynb"} for tag in previous_tags]

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

    # Get the branch that is checked out when the script starts,
    # so we can check it out again later.
    checked_out_branch = (
        subprocess.check_output(["git", "rev-parse", "--abbrev-ref", "HEAD"])
        .decode("utf-8")
        .strip()
    )

    tags = get_tags()
    if not tags:
        raise ValueError("No tags found")

    for tag in tags:
        print(f"Processing tag {tag}")
        checkout_ref(tag)
        copy_notebook(tag, dry_run=args.dry_run)
        copy_freeze_directory(tag, dry_run=args.dry_run)

    update_quarto_yaml(tags, dry_run=args.dry_run)

    # Clean up by checking out the branch that was checked out when the script started.
    checkout_ref(checked_out_branch)


if __name__ == "__main__":
    main()
