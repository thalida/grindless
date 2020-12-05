import os

VERSION = 1

SOURCE_DIR = os.path.realpath('./grindless')
CONFIGS_DIR = os.path.join(SOURCE_DIR, 'configs')
TEMPLATES_DIR = os.path.join(SOURCE_DIR, 'templates')
DIST_DIR = os.path.realpath('./builds')
ZIPS_DIR = os.path.realpath('./releases')
REGION_TEMPLATE_PATH = os.path.join(TEMPLATES_DIR, 'region.jinja')
DIST_REGION_FNS_DIR = os.path.join(DIST_DIR,  'data/grindless/functions/regions')
