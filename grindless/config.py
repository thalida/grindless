"""
Dev config settings for building and releasing
"""


import os

VERSION = '1.0.0'

SOURCE_DIR = os.path.realpath('./grindless')
SCFRIPTS_DIR = os.path.join(SOURCE_DIR, 'scripts')
CONFIGS_DIR = os.path.join(SOURCE_DIR, 'settings')
TEMPLATES_DIR = os.path.join(SOURCE_DIR, 'datapacks/grindless/templates')
DIST_DIR = os.path.realpath('./build')
ZIPS_DIR = os.path.realpath('./releases')
REGIONS_DIR = os.path.join(CONFIGS_DIR, 'regions')
REGION_TEMPLATE_PATH = os.path.join(TEMPLATES_DIR, 'region.jinja')
DIST_REGION_FNS_DIR = os.path.join(DIST_DIR,  'data/grindless/functions/regions')
