# -*- coding: utf-8 -*-
# flake8: noqa
# noreorder
"""
Pytube: a very serious Python library for downloading YouTube Videos.
"""
__title__ = 'pytube'
__version__ = '9.5.1'
__author__ = 'Nick Ficano'
__license__ = 'MIT License'
__copyright__ = 'Copyright 2019 Nick Ficano'

from modules.pytube.logging import create_logger
from modules.pytube.query import CaptionQuery
from modules.pytube.query import StreamQuery
from modules.pytube.streams import Stream
from modules.pytube.captions import Caption
from modules.pytube.contrib.playlist import Playlist
from modules.pytube.__main__ import YouTube

logger = create_logger()
logger.info('%s v%s', __title__, __version__)
