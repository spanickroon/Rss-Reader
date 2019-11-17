"""Conversion module to json"""
import json
from rssreader.parser import feed_parser


class JsonConversion(feed_parser.RssParser):
    """Class that converts rss to json"""
    def __init__(self, url: str, limit=None) -> None:
        super().__init__(url, limit)
        self.data = super().rss_parser_dict()

    def convert_to_json(self):
        """Method that converts rss to json"""
        return json.dumps(self.data, indent=4)
