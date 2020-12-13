"""
Helpers
=================================
refactor to be part of the datapack configs

.. autofunction:: read_yaml_file
"""

import yaml


TOOL_SELECTORS = {
    'ANY': 'any',
    'ANY_TOOL': 'any_tool',
}


def read_yaml_file(filename):
    with open(filename, 'r') as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
