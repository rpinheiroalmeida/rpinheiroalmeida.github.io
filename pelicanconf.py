#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Rodrigo Pinheiro'
SITENAME = "catch (Exception)"
# SITEURL = 'https://rpinheiroalmeida.github.io'
SITEURL = ''
BROWSER_COLOR = '#d9411e'

PATH = 'content'

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = 'pt_BR.UTF-8'
# LANG = pt_BR.UTF-8
# LANGUAGE = pt_BR:pt:en

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (
    ('github', 'https://github.com/rpinheiroalmeida'),
    ('twitter', 'https://twitter.com/_rodrigopa_'),
    ('linkedin', 'https://www.linkedin.com/in/rpinheiroalmeida')
)

DEFAULT_PAGINATION = 10

USE_FOLDER_AS_CATEGORY = True

USE_FOLDER_AS_CATEGORY = True
MAIN_MENU = True

MENUITEMS = (('Archives', '/archives.html'),
             ('Categories', '/categories.html'),
             ('Tags', '/tags.html'),)


OG_LOCALE = u'pt_BR'

SITETITLE = u'Catch code'
SITESUBTITLE = u'throw exception'
SITEDESCRIPTION = u'logger.info(exception)'

FEED_ALL_RSS = 'feeds.rss'
CATEGORY_FEED_RSS = 'feeds/%s.rss'
FEED_ALL_ATOM = 'feeds.atom'
CATEGORY_FEED_ATOM = 'feeds/%s.atom'
FEED_USE_SUMMARY = True

DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False

TAG_CLOUD_STEPS = 8
TAG_CLOUD_MAX_ITEMS = 100

FAVICON = '/images/favicon.ico'

# Plugins
# PLUGIN_PATH = './.plugins'
# PLUGINS = [
#         'gzip_cache',
#         'sitemap',
#         'related_posts',
#     ]

THEME = './temas/Flex'

# MD_EXTENSIONS = ['codehilite(noclasses=True, pygments_style=native)', 'extra']  # enable MD options

#Static Paths
# STATIC_PATHS = [
#     'output/audio',
#     'output/images',
#     'output/extra/robots.txt',
#     'output/extra/favicon.ico',
#     ]

# EXTRA_PATH_METADATA = {
#     'extra/robots.txt': {'/output/images/': 'robots.txt'},
#     'extra/favicon.ico': {'/output/images/': 'favicon.ico'},
#     }

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
