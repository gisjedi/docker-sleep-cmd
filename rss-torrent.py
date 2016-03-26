#!/usr/bin/env python

import logging
import feedparser
import sys

# Set up logger
logger = logging.getLogger(sys.argv[0])
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
sh = logging.StreamHandler()
sh.setLevel(logging.DEBUG)
sh.setFormatter(formatter)
logger.addHandler(sh)

# Parameter 1: RSS Feed
# Parameter 2: Optional target directory

logger.info('Launching download from rss feed: %s' % ' '.join(sys.argv[1:]))

feed_obj = feedparser.parse(sys.argv[1])

for entry in feed_obj.entries:
    print entry.title

