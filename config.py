import os

VERSION = 1
DIR_PATH = os.path.dirname(os.path.realpath(__file__))

SOURCE_DIR = os.path.realpath('./source')
CONFIGS_DIR = os.path.join(SOURCE_DIR, 'configs')
TEMPLATES_DIR = os.path.join(SOURCE_DIR, 'templates')

DIST_FOLDER = './dist'
DIST_DIR = os.path.realpath(DIST_FOLDER)
