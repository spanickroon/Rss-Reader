"""Conversion module to json"""

import json
from bs4 import BeautifulSoup

from rssreader.parser import feed_parser
from rssreader.exceptions import all_exceptions


class JsonConversion(feed_parser.RssParser):
    """Class that converts rss to json"""
    def __init__(self, url: str, limit=None) -> None:
        super().__init__(url, limit)

    def convert_to_json(self) -> str:
        """Method that converts rss to json"""
        return json.dumps(super().parse_news(), indent=4, ensure_ascii=False)
