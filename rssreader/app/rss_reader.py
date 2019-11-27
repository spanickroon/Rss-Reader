"""Entry point module"""

import logging

from rssreader.arguments import all_args, arg_verbose
from rssreader.parser import feed_parser
from rssreader.format_conversion import conversion_json as cv_json


class RssReader(all_args.Arguments):
    def __reaction_to_arguments(self) -> None:
        """
        Method that performs various actions
        depending on command line arguments
        """
        limit = self.args.limit
        source = self.args.source
        debug_string = "Start with arguments: " +\
            f"--limit: {limit}, " +\
            f"--json {self.args.json}, " +\
            f"--verbose {self.args.verbose}"

        logging.debug(debug_string)
        logging.debug(f"URL: {source}")
        logging.info(f"Get rss from {source}")

        if self.args.json:
            logging.info(f"Convert rss from {source} to json")
            feed_json = cv_json.JsonConversion(source, limit)
            return feed_json.convert_to_json()
        else:
            feed = feed_parser.RssParser(source, limit)
            logging.info("Show result of parsing")
            return feed.make_pretty_rss(feed.parse_news())

    def get_verbose(self):
        return arg_verbose.AppLogging.show_logs() if self.args.verbose else ""

    def run(self) -> None:
        """Application launch"""
        logging.info("Run app")
        return self.__reaction_to_arguments()


def main() -> None:
    """Main application method"""
    try:
        arg_verbose.AppLogging.log_setup()
        rss_app = RssReader()
        print(rss_app.run())
    except Exception as e:
        logging.error(e)
        print(e)
    finally:
        print(rss_app.get_verbose())
