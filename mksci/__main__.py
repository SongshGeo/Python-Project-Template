#!/usr/bin/env python
# -*-coding:utf-8 -*-
# Created date: 2022/3/1
# @Author  : Shuang Song
# @Contact   : SongshGeo@gmail.com
# GitHub   : https://github.com/SongshGeo
# Research Gate: https://www.researchgate.net/profile/Song_Shuang9

import logging
import os
import shutil
import sys
import textwrap

import click

# import mksci
# from . import __version__
# import mksci
from mksci import __version__

PKG_DIR = os.path.dirname(os.path.abspath(__file__))
PYTHON_VERSION = f"{sys.version_info.major}.{sys.version_info.minor}"
ROOT = os.getcwd()
log = logging.getLogger(__name__)


class ColorFormatter(logging.Formatter):
    colors = {
        "CRITICAL": "red",
        "ERROR": "red",
        "WARNING": "yellow",
        "DEBUG": "blue",
    }

    text_wrapper = textwrap.TextWrapper(
        width=shutil.get_terminal_size(fallback=(0, 0)).columns,
        replace_whitespace=False,
        break_long_words=False,
        break_on_hyphens=False,
        initial_indent=" " * 12,
        subsequent_indent=" " * 12,
    )

    def format(self, record):
        message = super().format(record)
        prefix = f"{record.levelname:<8} -  "
        if record.levelname in self.colors:
            prefix = click.style(prefix, fg=self.colors[record.levelname])
        if self.text_wrapper.width:
            # Only wrap text if a terminal width was detected
            msg = "\n".join(
                self.text_wrapper.fill(line) for line in message.splitlines()
            )
            # Prepend prefix after wrapping so that color codes don't affect length
            return prefix + msg[12:]
        return prefix + message


class State:
    """Maintain logging level."""

    def __init__(self, log_name="mksci", level=logging.INFO):
        self.logger = logging.getLogger(log_name)
        # Don't restrict level on logger; use handler
        self.logger.setLevel(1)
        self.logger.propagate = False

        self.stream = logging.StreamHandler()
        self.stream.setFormatter(ColorFormatter())
        self.stream.setLevel(level)
        self.stream.name = "MkSciStreamHandler"
        self.logger.addHandler(self.stream)


def add_options(opts):
    def inner(f):
        for i in reversed(opts):
            f = i(f)
        return f

    return inner


def verbose_option(f):
    def callback(ctx, _, value):
        state = ctx.ensure_object(State)
        if value:
            state.stream.setLevel(logging.DEBUG)

    return click.option(
        "-v",
        "--verbose",
        is_flag=True,
        expose_value=False,
        help="Enable verbose output",
        callback=callback,
    )(f)


def quiet_option(f):
    def callback(ctx, _, value):
        state = ctx.ensure_object(State)
        if value:
            state.stream.setLevel(logging.ERROR)

    return click.option(
        "-q",
        "--quiet",
        is_flag=True,
        expose_value=False,
        help="Silence warnings",
        callback=callback,
    )(f)


pass_state = click.make_pass_decorator(State, ensure=True)

common_options = add_options([quiet_option, verbose_option])


@click.group(context_settings={"help_option_names": ["-h", "--help"]})
@click.version_option(
    __version__,
    "-V",
    "--version",
    message=f"%(prog)s, version %(version)s from { PKG_DIR } (Python { PYTHON_VERSION })",
)
@common_options
def cli():
    """
    MkSci - Scientific Python Project automatic manager.
    """


@cli.command(name="new")
@click.option("--dictionary", default="", help="If create a new dictionary?")
@common_options
def new_command(dictionary):
    """Create a new SCI project in the current directory."""
    from mksci.commands import new

    new.new(dictionary)


if __name__ == "__main__":  # pragma: no cover
    cli()
