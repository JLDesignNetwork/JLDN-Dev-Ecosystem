#!/usr/bin/env python3
"""
* @lifecycle persistent
* @cleanup   manual
* @purpose   Validates JSON and JLDN ecosystem frontmatter.
"""

import os
import json
import sys


def validate_json_files(root_dir):
    errors = 0
    for dirpath, _, filenames in os.walk(root_dir):
        if ".git" in dirpath:
            continue
        for file in filenames:
            if file.endswith(".json"):
                filepath = os.path.join(dirpath, file)
                try:
                    with open(filepath, "r") as f:
                        json.load(f)
                except json.JSONDecodeError as e:
                    print(f"[ERROR] Invalid JSON in {filepath}: {e}")
                    errors += 1
                except Exception as e:
                    print(f"[ERROR] Could not read {filepath}: {e}")
                    errors += 1
    return errors


def validate_frontmatter(target_dir):
    if not os.path.exists(target_dir):
        return 0
    errors = 0
    required_tags = ["@lifecycle", "@cleanup"]
    for dirpath, _, filenames in os.walk(target_dir):
        for file in filenames:
            filepath = os.path.join(dirpath, file)
            with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()
                for tag in required_tags:
                    if tag not in content:
                        print(f"[ERROR] Missing '{tag}' in {filepath}")
                        errors += 1
    return errors


def main():
    root_dir = "."
    dev_eco_dir = os.path.join(root_dir, ".dev-ecosystem")

    print("Validating JSON files across workspace...")
    json_errors = validate_json_files(root_dir)

    print(f"\nValidating frontmatter in {dev_eco_dir}...")
    fm_errors = validate_frontmatter(dev_eco_dir)

    total_errors = json_errors + fm_errors
    if total_errors > 0:
        print(f"\nValidation failed with {total_errors} errors.")
        sys.exit(1)

    print("\nWorkspace validation passed successfully!")
    sys.exit(0)


if __name__ == "__main__":
    main()
