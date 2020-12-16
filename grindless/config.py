"""
Config
=================================

These global constants are used by the build and release scripts.
Learn more about :doc:`scripts <./scripts/index>`.


----

Globals
-------------

.. autodata:: grindless.config.CONFIG_DIR
    :annotation: = /abs/path/to/grindless-repo/grindless

.. autodata:: grindless.config.DIST_DIR
    :annotation: = <CONFIG_DIR>/../build

.. autodata:: grindless.config.DIST_REGION_FNS_DIR
    :annotation: = <DIST_DIR>/data/grindless/functions/regions

.. autodata:: grindless.config.REGIONS_DIR
    :annotation: = <SETTINGS_DIR>/regions

.. autodata:: grindless.config.REGION_TEMPLATE_PATH
    :annotation: = <TEMPLATES_DIR>/region.jinja

.. autodata:: grindless.config.SCRIPTS_DIR
    :annotation: = <SOURCE_DIR>/scripts

.. autodata:: grindless.config.SETTINGS_DIR
    :annotation: = <SOURCE_DIR>/settings

.. autodata:: grindless.config.SOURCE_DIR
    :annotation: = <CONFIG_DIR>/

.. autodata:: grindless.config.TEMPLATES_DIR
    :annotation: = <SOURCE_DIR>/datapacks/grindless/templates

.. autodata:: grindless.config.VERSION

.. autodata:: grindless.config.ZIPS_DIR
    :annotation: = <CONFIG_DIR>/../releases
"""

import pathlib
import os

VERSION = '1.0.0'
"""
Datapack Version

Used by: :ref:`release script <scripts-release>`
"""

CONFIG_DIR = str(pathlib.Path(__file__).parent.absolute())
"""
Directory the config file is located in

The paths below are built from this relative dir.
"""

SOURCE_DIR = str(pathlib.PurePath(CONFIG_DIR))
"""
Subdirectory which includes all of the core logic.

Used by: :ref:`build script <scripts-build>` and :ref:`release script <scripts-release>`
"""

DIST_DIR = str(pathlib.PurePath(CONFIG_DIR,  '../build'))
"""
Output directory of the built datapack. This folder is gitignored.

Used by: :ref:`build script <scripts-build>` and :ref:`release script <scripts-release>`
"""

ZIPS_DIR = str(pathlib.PurePath(CONFIG_DIR,  '../releases'))
"""
Output directory of the zipped datapack build. This folder is gitignored.

Used by: :ref:`release script <scripts-release>`
"""

DIST_REGION_FNS_DIR = os.path.join(DIST_DIR,  'data/grindless/functions/regions')
"""
Output directory of the built regions ``mcfunctions``.

Used by: :ref:`build script <scripts-build>`
"""

SCRIPTS_DIR = os.path.join(SOURCE_DIR, 'scripts')
"""
Holds all of the comandline-run scripts.

Used by: :ref:`build script <scripts-build>`
"""

SETTINGS_DIR = os.path.join(SOURCE_DIR, 'settings')
"""
Directory with all of the datapack settings.

Used by: :ref:`build script <scripts-build>` and :doc:`settings <settings/index>`
"""

REGIONS_DIR = os.path.join(SETTINGS_DIR, 'regions')
"""
Directory with all of the region specific settings.
Learn more about :doc:`regions <settings/regions/index>`.

Used by: :ref:`build script <scripts-build>`
"""

TEMPLATES_DIR = os.path.join(SOURCE_DIR, 'datapacks/grindless/templates')
"""
Directory with partial templates and methods.
Learn more about :doc:`templates <datapacks/grindless/templates/index>`.

Used by: :ref:`build script <scripts-build>`
"""

REGION_TEMPLATE_PATH = os.path.join(TEMPLATES_DIR, 'region.jinja')
"""
Absolute path to the region template.
Learn more about :doc:`templates <datapacks/grindless/templates/index>`.

Used by: :ref:`build script <scripts-build>`
"""
