#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'PoiScript'
SITENAME = 'Solomon'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = 'zh'

THEME = 'theme'

STATIC_PATHS = ['extra/favicon.ico', 'extra/icon.png']

DEFAULT_PAGINATION = False

PLUGIN_PATHS = ["plugins"]
PLUGINS = [
    "amp_markdown_reader"
]
