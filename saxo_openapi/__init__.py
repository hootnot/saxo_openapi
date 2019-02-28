# -*- coding: utf-8 -*-

"""Top-level package for SAXO OpenAPI."""

__author__ = """Feite Brekeveld"""
__email__ = 'f.brekeveld@gmail.com'
__version__ = '0.1.0'

# Version synonym
VERSION = __version__

# Set default logging handler to avoid "No handler found" warnings.
import logging
try:
    from logging import NullHandler
except ImportError:
    class NullHandler(logging.Handler):
        def emit(self, record):
            pass

logging.getLogger(__name__).addHandler(NullHandler())

from .saxo_openapi import API
from .exceptions import OpenAPIError
