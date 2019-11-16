from rssreader.arguments import all_args


class RssReader(all_args.Arguments):
    def run(self) -> None:
        print(self.args)


def main() -> None:
    try:
        rss_app = RssReader()
        rss_app.run()
    except Exception as e:
        print(e)
