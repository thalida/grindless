from pprint import pprint
import yaml
from collections import OrderedDict
import os
import pathlib
import shutil
from jinja2 import Environment, FileSystemLoader
from inspect import getmembers, isfunction

import config
import helpers
import source.templates.methods as methods

from source.configs.regions.base_region import BaseRegion
from source.configs.regions.badlands import Badlands

env = Environment(
    variable_start_string='<<',
    variable_end_string='>>',
    comment_start_string='/*',
    comment_end_string='*/',
    autoescape=False,
    trim_blocks=True,
    lstrip_blocks=True,
    loader=FileSystemLoader(config.SOURCE_DIR),
)

for func_name, fn in getmembers(methods, isfunction):
    env.globals[func_name] = fn

def run_items_create():
    all_configs = helpers.get_datapack_configs()
    all_region_configs = all_configs['regions']
    all_items = {}

    for region, config in all_region_configs.items():
        for tool, tool_stanza in config['resources'].items():
            for subtype, subtype_stanza in tool_stanza.items():
                for item, gives in subtype_stanza['items'].items():
                    if item not in all_items:
                        all_items[item] = {}

                    if tool not in all_items[item]:
                        all_items[item][tool] = {}

                    if subtype not in all_items[item][tool]:
                        all_items[item][tool][subtype] = gives / BaseRegion.material_multipliers['items']['default']
                    # print(region, tool, subtype, item, gives)

    all_items = dict(OrderedDict(sorted(all_items.items())))
    with open('./source/configs/items.yaml', 'w') as file:
        documents = yaml.dump(all_items, file)

if __name__ == '__main__':
    # run_items_create()
    all_configs = helpers.get_datapack_configs()

    region_template_path = config.REGION_TEMPLATE_PATH.replace(f"{config.SOURCE_DIR}/", '')
    region_template = env.get_template(region_template_path)

    pathlib.Path(config.DIST_REGION_FNS_DIR).mkdir(parents=True, exist_ok=True)
    output_path = os.path.join(config.DIST_REGION_FNS_DIR, f'badlands.mcfunction')
    output = region_template.render(**all_configs, region=Badlands().create_config())

    with open(output_path, "w") as fh:
        fh.write(output)