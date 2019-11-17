import logging
from rssreader.arguments import all_args, arg_verbose


class RssReader(all_args.Arguments):
    def run(self) -> None:
        logging.info("Run app")


def main() -> None:
    try:
        arg_verbose.AppLogging.log_setup()
        rss_app = RssReader()
        rss_app.run()
    except Exception as e:
        logging.error(e)
        print(e)
