# -*- coding: utf-8 -*-

"""Top-level package for SAXO OpenAPI."""

# Set default logging handler to avoid "No handler found" warnings.
from .saxo_openapi import API   # noqa F401
from .exceptions import OpenAPIError  # noqa F401

import logging
try:
    from logging import NullHandler
except ImportError:
    class NullHandler(logging.Handler):
        def emit(self, record):
            pass

logging.getLogger(__name__).addHandler(NullHandler())


__title__ = "Saxo OpenAPI API Wrapper"
__author__ = """Feite Brekeveld"""
__email__ = 'f.brekeveld@gmail.com'
__version__ = '0.6.0'
__copyright__ = "Copyright 2019 Feite Brekeveld"


# Version synonym
VERSION = __version__
