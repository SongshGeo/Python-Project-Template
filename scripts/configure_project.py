#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Project configuration script with gettext-based internationalization.

This script initializes a Python project by updating pyproject metadata,
GitHub workflow placeholders, README, and CHANGELOG. Prompts are localized
using gettext with English as the default language.

Usage:
    python scripts/configure_project.py

Examples:
    $ python scripts/configure_project.py
    Project name: my-awesome-project
    Project description: An awesome Python project

    # via Makefile
    $ make configure-project
"""

import argparse
import gettext
import os
from pathlib import Path

import questionary

LOCALE_DIR = Path(__file__).parent / "locales"
DEFAULT_LANG = "en"
SUPPORTED_LANGS = {"en", "zh"}


def get_translator() -> gettext.NullTranslations:
    """
    Load a gettext translator based on LANG or LANGUAGE environment variables.

    English is used as the default fallback when translations are unavailable.
    """
    lang_env = os.environ.get("LANGUAGE") or os.environ.get("LANG") or DEFAULT_LANG
    lang_code = lang_env.split(".")[0].split("_")[0]
    language = lang_code if lang_code in SUPPORTED_LANGS else DEFAULT_LANG
    try:
        translator = gettext.translation(
            "messages",
            localedir=LOCALE_DIR,
            languages=[language],
            fallback=True,
        )
    except Exception:
        translator = gettext.NullTranslations()
    return translator


_ = get_translator().gettext

README_TEMPLATE = """
# {title}

{description}
"""


def configure_files(project_name: str, project_description: str) -> None:
    """
    Configure project information in configuration files.

    This function updates the project name and description in various
    configuration files including pyproject.toml ([project] section) and
    GitHub workflow files.

    Args:
        project_name: The name of the project to set
        project_description: The description of the project to set

    Example:
        >>> configure_files("my-awesome-project", "An awesome Python project")
        ✓ Updated pyproject.toml
        ✓ Updated .github/workflows/release-please.yml
    """
    # Configuration paths
    files_to_update = {
        "pyproject.toml": [
            ('name = "songshgeo"', 'name = "' + project_name + '"'),
            ('description = "Template"', 'description = "' + project_description + '"'),
        ],
        ".github/workflows/release-please.yml": [
            ("${project_name}", project_name),
        ],
    }

    # Special handling for pyproject.toml
    pyproject_path = Path("pyproject.toml")
    if pyproject_path.exists():
        content = pyproject_path.read_text(encoding="utf-8")

        # Update [project] name and description
        content = content.replace('name = "songshgeo"', 'name = "' + project_name + '"')
        content = content.replace(
            'description = "Template"', 'description = "' + project_description + '"'
        )

        pyproject_path.write_text(content, encoding="utf-8")
        print(_("✓ Updated pyproject.toml"))

    # pyproject.toml is handled above
    for file_path, replacements in files_to_update.items():
        if file_path == "pyproject.toml":
            continue
        path = Path(file_path)
        if path.exists():
            content = path.read_text(encoding="utf-8")
            for old, new in replacements:
                content = content.replace(old, new)
            path.write_text(content, encoding="utf-8")
            print(_("✓ Updated {path}").format(path=file_path))
        else:
            print(_("! Warning: file not found {path}").format(path=file_path))


def setup_description_files(title: str, description: str) -> None:
    """
    Setup project description files.

    This function clears the CHANGELOG.md file and creates a new
    README.md with the provided title and description.

    Args:
        title: The project title
        description: The project description

    Example:
        >>> setup_description_files("My Project", "A great project")
        # Creates README.md with template and clears CHANGELOG.md
    """
    Path("CHANGELOG.md").write_text("", encoding="utf-8")
    Path("README.md").write_text(
        README_TEMPLATE.format(title=title, description=description),
        encoding="utf-8",
    )


def parse_args(argv: "list[str] | None" = None) -> argparse.Namespace:
    """
    Parse command-line arguments for the configuration script.

    Args:
        argv: Optional argument list (defaults to ``sys.argv`` when ``None``).

    Returns:
        The parsed namespace with ``name`` and ``description`` attributes.
    """
    parser = argparse.ArgumentParser(
        description=_("Configure project metadata (name, description)."),
    )
    parser.add_argument("--name", default=None, help=_("Project name"))
    parser.add_argument("--description", default=None, help=_("Project description"))
    return parser.parse_args(argv)


def main(argv: "list[str] | None" = None) -> None:
    """
    Main entry point for the project configuration script.

    When ``--name`` and ``--description`` are both supplied the script runs
    non-interactively (used by the ``setup-project`` Claude Code skill and by
    CI); otherwise it falls back to interactive ``questionary`` prompts.

    Flow:
        1. Resolve project name and description (from args or prompts)
        2. Update the [project] section of pyproject.toml
        3. Update GitHub workflow files
        4. Create/update README.md
        5. Clear CHANGELOG.md

    Example:
        $ python scripts/configure_project.py --name my-project \\
            --description "A sample project"
        ✓ Updated pyproject.toml
        ✓ Updated .github/workflows/release-please.yml
        ✨ Project configuration completed!
    """
    args = parse_args(argv)
    print(_("Starting project configuration..."))

    if args.name and args.description:
        project_name = args.name
        project_description = args.description
    else:
        project_name = (
            args.name
            or questionary.text(
                _("Project name:"),
                validate=lambda text: len(text) > 0,
            ).ask()
        )

        project_description = (
            args.description
            or questionary.text(
                _("Project description:"),
                validate=lambda text: len(text) > 0,
            ).ask()
        )

    configure_files(project_name, project_description)
    setup_description_files(project_name, project_description)
    print(_("\n✨ Project configuration completed!"))


if __name__ == "__main__":
    main()
