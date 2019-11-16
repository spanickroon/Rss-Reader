"""A module that sets command line arguments"""
import argparse
from rssreader import cnf


class ArgumentParserError(Exception):
    """The exception class

    The exception that is thrown when
    the arguments are entered incorrectly

    """
    def __init__(self, message):
        self.message = message


class ThrowingArgumentParser(argparse.ArgumentParser):
    """
    The class that causes exclusion by overloading
    method error() of class ArgumentParser
    """
    def error(self, message):
        """
        Method that throws an exception in response
        to a built-in error of the module argparse
        """
        raise ArgumentParserError(message)


class Arguments:
    """A class that sets command line arguments"""
    def __init__(self):
        parser = ThrowingArgumentParser(
            prog="rss_reader",
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
