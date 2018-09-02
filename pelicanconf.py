#!/usr/bin/env python

from os.path import expanduser, join

AUTHOR = "Elliot Marsden"
SITENAME = "Elliot Marsden"
SITEURL = ""

PATH = "content"

TIMEZONE = "Europe/Amsterdam"

DEFAULT_LANG = "en"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
)

# Social widget
SOCIAL = (
    ("GitHub", "https://github.com/eddiejessup"),
    # ("Twitter", "https://twitter.com/EddieJessup"),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# Custom:

PLUGIN_PATHS = ["pelican-plugins"]
PLUGINS = ["render_math", "ipynb.liquid"]

STATIC_PATHS = ["images", "pdfs"]

DISPLAY_PAGES_ON_MENU = True
PAGE_PATHS = ["pages"]
MENUITEMS = [
    ("CV", "/pdfs/cv.pdf"),
]
TYPOGRIFY = False
SUMMARY_MAX_LENGTH = 50

THEME = "notmyidea"
