"""A module that sets command line arguments"""

import argparse
from rssreader import cnf
from rssreader.exceptions.all_exceptions import ThrowingArgumentParser


class Arguments:
    """A class that sets command line arguments"""
    def __init__(self) -> None:
        parser = ThrowingArgumentParser(
            prog=cnf.__package__,
            description="Pure Python command-line RSS reader."
        )
        parser.add_argument(
            "--json",
            help="Print result as JSON in stdout",
            action="store_true"
        )
        parser.add_argument(
            "--limit",
            help="Limit news topics if this parameter is provided",
            type=int
        )
        parser.add_argument(
            "--verbose",
            help="Outputs verbose status messages",
            action="store_true"
        )
        parser.add_argument(
            "--version",
            help="Print version info",
            action="version",
            version=cnf.__version__
        )
        parser.add_argument(
            "source",
            help="RSS URL",
            type=str
        )
        self.args = parser.parse_args()
