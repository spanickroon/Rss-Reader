import logging
from rssreader.arguments import all_args, arg_verbose


class RssReader(all_args.Arguments):
    def __reaction_to_arguments(self):
        if self.args.verbose:
            print(arg_verbose.AppLogging.show_logs())
        if self.args.json:
            pass
        else:
            pass

    def run(self) -> None:
        logging.info("Run app")
        self.__reaction_to_arguments()


def main() -> None:
    try:
        arg_verbose.AppLogging.log_setup()
        rss_app = RssReader()
        rss_app.run()
    except Exception as e:
        logging.error(e)
        print(e)
