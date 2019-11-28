from os import path

from setuptools import setup, find_packages
from rssreader import cnf


def get_path_to_long_description(file_name):
    this_directory = path.abspath(path.dirname(__file__))

    with open(
        path.join(this_directory, "rssreader", "documentation", file_name),
        encoding="utf-8"
            ) as f:
        long_description = f.read()

    return long_description


setup(
    name=cnf.__package__,
    version=cnf.__version__,
    description="One-shot command-line RSS reader",
    long_description=get_path_to_long_description("manual.md"),
    long_description_content_type="text/markdown",
    author="Nikita Koznev",
    author_email="nikitakoznev@gmail.com",
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=["bs4", "feedparser", "nose", "pymongo"],
    entry_points={
        "console_scripts":
            [f"{cnf.__package__} = rssreader.__main__:main"]
        }
)
