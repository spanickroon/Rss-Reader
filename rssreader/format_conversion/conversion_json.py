"""Conversion module to json"""

import json
from bs4 import BeautifulSoup
from rssreader.parser import feed_parser


class JsonConversion(feed_parser.RssParser):
    """Class that converts rss to json"""
    def __init__(self, url: str, limit=None) -> None:
        super().__init__(url, limit)

    def __parse_news(self) -> list:
        """
        Method that parses the news and makes them a template for the future
        """
        self.html_news = super()._check_connection_and_getting_rss()
        self.limit = super()._check_limit()

        feed = self.html_news.feed.title
        parsing_news = []

        for entry in self.html_news.entries[:self.limit]:
            temp_dict = {
                'feed': feed,
                'title': entry.title.replace("&#39;", "'"),
                'data': entry.published,
                'link': entry.link,
                'links': entry.links,
                'description': BeautifulSoup(
                    entry.summary, features="html.parser"
                    ).text,
                'title_detail': {
                    'type': entry.title_detail.type,
                    'language': entry.title_detail.language,
                    'base': entry.title_detail.base,
                    'value': entry.title_detail.value.replace("&#39;", "'")
                    }
            }
            parsing_news.append(temp_dict)

        return parsing_news

    def convert_to_json(self) -> json:
        """Method that converts rss to json"""
        return json.dumps(self.__parse_news(), indent=4, ensure_ascii=False)
