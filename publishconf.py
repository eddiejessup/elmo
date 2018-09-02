#!/usr/bin/env python

# This file is used when you run `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *  # noqa

SITEURL = "http://elliotmarsden.com"
RELATIVE_URLS = False

FEED_ALL_ATOM = "feeds/all.atom.xml"
CATEGORY_FEED_ATOM = "feeds/%s.atom.xml"

DELETE_OUTPUT_DIRECTORY = True

# These items are often useful when publishing.

#GOOGLE_ANALYTICS = ""
