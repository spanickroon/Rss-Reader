"""Tests for rssreader.format_conversion.conversion_json module"""

import unittest
import feedparser
from unittest.mock import patch
from os import path


from rssreader.format_conversion import conversion_json
from rssreader.exceptions import all_exceptions


class JsonConversionTestCase(unittest.TestCase):
    def setUp(self):
        with open(
                path.join("tests", "unit", "data", "test_correct.rss"),
                "r") as rf:
            self.url = rf.read()

        self.test_feed_json = conversion_json.JsonConversion(self.url, 1)

    def test_convert_to_json(self):
        with open(path.join(
                "tests",
                "unit",
                "data",
                "test_convert_to_json.txt"), "r") as rf:
            answer = rf.read()

        self.assertEqual(
            self.test_feed_json.convert_to_json(),
            answer
        )


if __name__ == "__main__":
    unittest.main()
