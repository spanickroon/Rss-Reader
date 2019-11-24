"""Module that get a rss from the news portal"""

import feedparser
from bs4 import BeautifulSoup
from rssreader.exceptions import all_exceptions


class RssParser:
    """The class that receives the news in rss format"""
    def __init__(self, url: str, limit: int = None) -> None:
        self.url = url
        self.limit = limit
        self.articles = []

    @property
    def limit(self) -> int:
        """A property that returns the limit value"""
        return self.__limit

    @limit.setter
    def limit(self, value) -> None:
        """A property that checks for a negative value"""
        self.__limit = value if value is None or value > 0 else 0

    def _check_limit(self) -> int:
        """Function that checks the maximum limit value"""
        self.count_news = len(self.html_news.entries)

        if self.limit is not None:
            return min(self.limit, self.count_news)
        else:
            return self.count_news

    def _check_connection_and_getting_rss(self) -> dict:
        """
        Function that checks the possibility of receiving news and,
        if successful, receives them
        """
        html_news = feedparser.parse(self.url)

        if html_news.bozo == 1:
            err_msg = "Check your link or internet connection"
            raise all_exceptions.InvalidLinkOrInternetConnectionError(err_msg)

        return html_news

    def __parse_news(self) -> list:
        """
        Function that returns a list of news that was received by parsing rss
        """
        self.html_news = self._check_connection_and_getting_rss()
        self.limit = self._check_limit()

        parsing_news = []
        feed = self.html_news.feed.title

        for entry in self.html_news.entries[:self.limit]:
            temp_dict = {
                'Feed': feed,
                'Title': entry.title.replace("&#39;", "'"),
                'Data': entry.published,
                'Link': entry.link,
                'Description': BeautifulSoup(
                    entry.summary, features="html.parser"
                    ).text,
                'Links': [link["url"] for link in entry.media_content]
            }
            parsing_news.append(temp_dict)

        return parsing_news

    def __find_type_link(self, link) -> str:
        """
        Function that determines the type of file that is located at the link
        """
        return "(image)" if link.find(".mp4") == -1 else "(video)"

    def __make_pretty_links(self, link, links) -> str:
        """
        The function that returns the string in which the numeric
        representation of all links from the news is located
        """
        links_list = []
        len_list = 0

        if isinstance(link, list):
            len_list = len(link)
            for iter in enumerate(link):
                if iter[1]:
                    links_list.append(f"[{(iter[0] + 1)}]: {iter[1]}(link)")
        elif link:
            len_list = 1
            links_list.append(f"[1]: {link}(link)")

        if isinstance(links, list):
            for iter in enumerate(links):
                if iter[1]:
                    type_link = self.__find_type_link(iter[1])
                    links_list.append(
                        f"[{(iter[0]+1+len_list)}]: {iter[1]}{type_link}"
                        )
        elif links:
            type_link = self.__find_type_link(links)
            links_list.append(f"[{len_list + 1}]: {links}{type_link}")

        return "\n".join(links_list)

    def make_pretty_rss(self) -> str:
        """
        Function that returns the final representation
        of news that was obtained from the rss link
        """
        news = self.__parse_news()
        pretty_string = []

        for article in news:
            links = self.__make_pretty_links(
                        article['Link'],
                        article['Links']
                        )

            pretty_string.append(
                f"\nFeed: {article['Feed']}\n\nTitle: {article['Title']} \
                \nData: {article['Data']}\nLink: {article['Link']} \
                \n\n{article['Description']}\n\nLinks:\n{links}\n\n"
            )
        return "".join(pretty_string)
