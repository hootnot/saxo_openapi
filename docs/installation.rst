Introduction
============

The :mod:`saxo_openapi` package offers an API to the SAXO OpenAPI REST service.
To use the REST-API-service you will need a *token* and an *account*. This
applies for both *live*  and *practice* accounts. For details check www.developer.saxo_.

.. _www.developer.saxo: https://www.developer.saxo


Install
-------

Install the latest development version from github::

    $ pip install git+https://github.com/hootnot/saxo_openapi.git


Before installing, consider using *virtual environments* to create isolated
Python environments and install here.

.. code-block:

   $ python3.6 -m venv <envdirname-of-your-choice>
   $ . ./<envdirname-of-your-choice>/bin/activate
   $ pip install git+https://github.com/hootnot/saxo_openapi.git
