Changelog
=========

[Unreleased]
------------

New Features
~~~~~~~~~~~~

-  Implement referencedata/currencypairs endpoint, see issue #25

Administration and Chores
~~~~~~~~~~~~~~~~~~~~~~~~~

-  [requirements\_dev] require pip version 23.3.1

v0.8.3 (2023-11-01)
-------------------

Administration and Chores
~~~~~~~~~~~~~~~~~~~~~~~~~

-  update wheel version to 0.41.3

-  fix travis link from .org -> .com

v0.8.1 (2021-12-19)
-------------------

Administration and Chores
~~~~~~~~~~~~~~~~~~~~~~~~~

-  MANIFEST.in added

-  pip version adjustment

v0.8.0 (2021-07-14)
-------------------

Bug Fixes
~~~~~~~~~

-  endpoint missing / added

Administration and Chores
~~~~~~~~~~~~~~~~~~~~~~~~~

-  [travis] bring python versions in sync with tox.ini

-  [tox] devrequirements.txt added

-  [tox] tox.ini changes

v0.7.0 (2021-02-23)
-------------------

Bug Fixes
~~~~~~~~~

-  [streaming quotes] fixed to handle multiple messages bundled in 1
   websocket message

   BREAKING CHANGE: decode\_ws\_msg() is now a generator returning 1 or
   more decoded messages. See documentation for details.

Documentation Changes
~~~~~~~~~~~~~~~~~~~~~

-  [decode\_ws\_msg] updated for change

v0.6.0 (2019-09-16)
-------------------

New Features
~~~~~~~~~~~~

-  [order endpoints] added support for the ManualOrder attribute

   BREAKING CHANGE: SAXO OpenApi will require this attribute in the
   orderbodies, see:
   https://www.developer.saxo/excel/blog/updated-requirements-for-order-placement?phrase=ManualOrder

Style Fixes
~~~~~~~~~~~

-  fixed flake8 style issues

Documentation Changes
~~~~~~~~~~~~~~~~~~~~~

-  [sphinx config] fixed typo

v0.5.0 (2019-09-10)
-------------------

New Features
~~~~~~~~~~~~

-  [endpoints] chart endpoints

   addition of all chart endpoint classes

Documentation Changes
~~~~~~~~~~~~~~~~~~~~~

-  [endpoints] chart endpoints documentation

   all chart endpoint classes documentation
-  various doc/docstring updates

v0.4.1 (2019-05-23)
-------------------

New Features
~~~~~~~~~~~~

-  [endpoints] eventnotificationservices

   addition all eventnotificationservices endpoint classes
-  [definitions] activities and reportformats

   addition of definitions for 'activities' and 'reportformats'

Bug Fixes
~~~~~~~~~

-  corrected config causing broken build

   replace auto-changelog

Documentation Changes
~~~~~~~~~~~~~~~~~~~~~

-  [endpoints] eventnotificationservices

   addition all eventnotificationservices endpoint classes

v0.3.1 (2019-05-04)
-------------------

v0.3.0 (2019-05-04)
-------------------
