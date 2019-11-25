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

        if self.args.verbose:
            return arg_verbose.AppLogging.show_logs()
        if self.args.json:
            logging.info(f"Convert rss from {source} to json")
            feed_json = cv_json.JsonConversion(source, limit)
            return feed_json.convert_to_json()
        else:
            logging.info(f"Get rss from {source}")
            feed = feed_parser.RssParser(source, limit)
            return feed.make_pretty_rss(feed.parse_news())

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
