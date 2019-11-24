from setuptools import setup, find_packages
from rssreader import cnf

setup(
    name=cnf.__package__,
    version=cnf.__version__,
    description="One-shot command-line RSS reader",
    long_description="Program that helps to get files \
                    from various news portals",
    author="Nikita Koznev",
    author_email="nikitakoznev@gmail.com",
    packages=find_packages(),
    python_requires='>=3.8',
    install_requires=['bs4', 'feedparser'],
    entry_points={
        'console_scripts':
            [f'{cnf.__package__} = rssreader.__main__:main']
        }
)
