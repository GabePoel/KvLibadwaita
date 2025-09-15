#!/usr/bin/env python3
import argparse

from builder import __version__
from builder.helpers import available_color_schemes
from builder.utils import Gradience


def create_parser():
    parser = argparse.ArgumentParser(
        description="Gradience, build tool for override KvLibadwaita colors"
    )
    parser.add_argument(
        "--theme",
        type=str,
        choices=available_color_schemes(),
        default="catppuccin_mocha",
        dest="color_scheme",
        help="Color scheme name"
    )
    parser.add_argument(
        "--custom",
        type=str,
        help="Full path to your.json file which contains custom base16 theme"
    )
    parser.add_argument(
        "-v",
        "--version",
        action='version',
        version=__version__
    )

    return parser


def main():
    # init cmd args parser:
    parser = create_parser()
    args = parser.parse_args()

    gradience = Gradience(color_scheme=args.color_scheme, custom=args.custom)
    gradience.mktheme()


if __name__ == "__main__":
    main()
