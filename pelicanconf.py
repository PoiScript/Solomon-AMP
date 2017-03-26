#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# Basic settings
SITENAME = 'Solomon'
SITEURL = 'https://amp.poi.works'
PATH = 'content'
IGNORE_FILES = ['about.md', 'link.md']
PLUGIN_PATHS = ["plugins"]
PLUGINS = ["amp_markdown_reader"]

# URL settings
TAG_URL = 'tag/{slug}.html'
TAG_URL_SAVE_AS = 'tag/{slug}.html'
TAGS_SAVE_AS = ''
ARTICLE_URL = 'post/{slug}.html'
ARTICLE_SAVE_AS = 'post/{slug}.html'
ARCHIVES_SAVE_AS = 'archive.html'
AUTHOR_URL = ''
AUTHOR_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
CATEGORIES_SAVE_AS = ''

# Time and Data
TIMEZONE = 'Asia/Shanghai'

# Template pages
DIRECT_TEMPLATES = ['index', 'tags', 'archives']

# Metadata
AUTHOR = 'PoiScript'

# Feed Settings
FEED_DOMAIN = None
FEED_RSS = None
FEED_ATOM = None
FEED_ALL_RSS = None
FEED_ALL_ATOM = None
AUTHOR_FEED_RSS = None
AUTHOR_FEED_ATOM = None
TAG_FEED_RSS = None
TAG_FEED_ATOM = None
CATEGORY_FEED_RSS = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_RSS = None
TRANSLATION_FEED_ATOM = None

# Pagination
DEFAULT_PAGINATION = False

# Translations
DEFAULT_LANG = 'zh'

# Themes
THEME = 'theme/solomon_amp'
THEME_STATIC_DIR = ''

# Extra
NON_AMP_SITEURL = 'https://poi.works/#'
GITHUB_ISSUE_URL = 'https://github.com/PoiScript/Solomon-Post/issues'
