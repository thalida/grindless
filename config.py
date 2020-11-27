import os

VERSION = 1
DIR_PATH = os.path.dirname(os.path.realpath(__file__))

SOURCE_DIR = os.path.realpath('./source')
CONFIGS_DIR = os.path.join(SOURCE_DIR, 'configs')
TEMPLATES_DIR = os.path.join(SOURCE_DIR, 'templates')

DIST_FOLDER = './dist'
DIST_DIR = os.path.realpath(DIST_FOLDER)

REGION_TEMPLATE_PATH = os.path.join(TEMPLATES_DIR, 'region.jinja')
REGIONS_FNS_PATH = 'data/grindless/functions/regions'
SOURCE_REGION_FNS_DIR = os.path.join(SOURCE_DIR, REGIONS_FNS_PATH)
DIST_REGION_FNS_DIR = os.path.join(DIST_DIR, REGIONS_FNS_PATH)
