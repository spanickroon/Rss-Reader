"""
Module that get a rss from the news portal
Will be rewritten in v2.1, due to the slow operation of the methods
"""
import feedparser
from bs4 import BeautifulSoup
from pprint import pprint


class InternetConnectionError(Exception):
    """
    does not work
    will be fixed in v2.1
    """
    def __init__(self, message):
        self.message = message


class InvalidLinkError(Exception):
    """The exception class

    The exception that is thrown when
    the link are entered incorrectly

    """
    def __init__(self, message):
        self.message = message


class RssParser:
    """Will be rewritten in v2.1"""
    def __init__(self, url: str, limit=None) -> None:
        self.url = url
        self.limit = limit
        self.articles = []

    @property
    def limit(self):
        return self.__limit

    @limit.setter
    def limit(self, value):
        self.__limit = value if value is not None and value > 0 else 0

    def __check_connection(self):
        try:
            self.news = feedparser.parse(self.url)

            if self.news.bozo == 1:
                raise InvalidLinkError("Invalid news link")

            self.count_news = len(self.news.entries)
            self.limit = min(self.limit, self.count_news)
        except AttributeError:
            raise InternetConnectionError("No internet connection")

    def __adding_data_dict(self, iterator):
        soup = BeautifulSoup(iterator.summary, features="html.parser")
        return {"Title": str(iterator.title).replace("&#39;", "'"),
                "Date": iterator.published,
                "Link": iterator.link,
                "Description": soup.text,
                "Links": {
                    "Source": iterator.links[0]["href"],
                    "Img": [
                        link.get("src")
                        for link in soup.find_all("img") if link.get("src")
                    ]
                }}

    def __parse_news(self) -> None:
        self.__check_connection()
        for entry in self.news.entries:
            self.articles.append(self.__adding_data_dict(entry))

    def __adding_data_list(self, iterator, entry) -> None:
        parameter_list = [
            f"\nTitle: {entry['Title']}",
            f"Date: {entry['Date']}",
            f"Link: {entry['Link']}\n",
            f"{entry['Description']}\n",
            f"Links:\n[1]: {entry['Links']['Source']} (link)"
        ]
        for string in parameter_list:
            iterator.append(string)

    def show_rss(self) -> str:
        self.__parse_news()
        result_rss = [f"Feed: {self.news.feed.title}"]

        for entry in self.articles[:self.limit]:
            self.__adding_data_list(result_rss, entry)

            for img in enumerate(entry['Links']['Img']):
                result_rss.append(f"[{img[0]+2}]: {img[1]} (image)")

        return "\n".join(result_rss)

    def rss_parser_dict(self):
        self.show_rss()
        return {
            "Feed": self.news.feed.title,
            "Url": self.url,
            "News": self.articles[:self.limit]
        }
