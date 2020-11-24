import os

VERSION = 1

DIR_PATH = os.path.dirname(os.path.realpath(__file__))
SOURCE_DIR = os.path.realpath('./source')
DIST_FOLDER = './dist'
DIST_DIR = os.path.realpath(DIST_FOLDER)
TEMPLATES_DIR = os.path.join(SOURCE_DIR, 'templates')

datapack_settings = {
    "ticks_per_second": 20,
    "wait_seconds": 10,
    "button": {
        "name": "grind",
        "activation_radius": 4,
    }
}
datapack_settings['wait_ticks'] = datapack_settings.get('ticks_per_second', 20) * datapack_settings.get('wait_seconds', 0)