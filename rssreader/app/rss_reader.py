from rssreader.arguments import all_args, arg_verbose


class RssReader(all_args.Arguments, arg_verbose.AppLogging):
    def __init__(self):
        arg_verbose.AppLogging.log_setup()

    def run(self) -> None:
        pass


def main() -> None:
    try:
        rss_app = RssReader()
        rss_app.run()
    except Exception as e:
        print(e)
