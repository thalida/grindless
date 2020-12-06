"""
Config
=================================

.. currentmodule:: grindless.config

Dev config settings for building and releasing

.. literalinclude:: /../grindless/config.py
   :language: python
   :lines: 30-

.. autodata:: VERSION
.. autodata:: SOURCE_DIR
    :annotation: = /abs/path/to/grindless/grindless
.. autodata:: SCRIPTS_DIR
    :annotation: = /abs/path/to/grindless/grindless/scripts
.. autodata:: CONFIGS_DIR
    :annotation: = /abs/path/to/grindless/grindless/settings
.. autodata:: TEMPLATES_DIR
    :annotation: = /abs/path/to/grindless/grindless/datapacks/grindless/templates
.. autodata:: DIST_DIR
    :annotation: = /abs/path/to/grindless/grindless/datapacks/grindless/templates
.. autodata:: ZIPS_DIR
    :annotation: = /abs/path/to/grindless/grindless/datapacks/grindless/templates
"""

import os

VERSION = '1.0.0' #: 
SOURCE_DIR = os.path.realpath('./grindless') #:
SCRIPTS_DIR = os.path.join(SOURCE_DIR, 'scripts') #:
CONFIGS_DIR = os.path.join(SOURCE_DIR, 'settings') #:
TEMPLATES_DIR = os.path.join(SOURCE_DIR, 'datapacks/grindless/templates') #:
DIST_DIR = os.path.realpath('./build') #:
ZIPS_DIR = os.path.realpath('./releases') #:
REGIONS_DIR = os.path.join(CONFIGS_DIR, 'regions') #:
REGION_TEMPLATE_PATH = os.path.join(TEMPLATES_DIR, 'region.jinja') #:
DIST_REGION_FNS_DIR = os.path.join(DIST_DIR,  'data/grindless/functions/regions')  #:
