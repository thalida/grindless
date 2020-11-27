import os
import yaml
import pathlib
from inspect import getmembers, isclass

import config
import source.configs.regions as region_configs

def read_yaml_file(filename):
    with open(filename, 'r') as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)

def get_datapack_configs():
    datapack_configs = {
        "datapack": {},
        "scoreboards": {},
        "gather": {},
        "regions": {},
    }

    datapack_configs["datapack"] = read_yaml_file(os.path.join(config.CONFIGS_DIR, 'datapack.yaml'))
    datapack_configs["scoreboards"] = read_yaml_file(os.path.join(config.CONFIGS_DIR, 'scoreboards.yaml'))
    datapack_configs["gather"] = read_yaml_file(os.path.join(config.CONFIGS_DIR, 'gather.yaml'))
    datapack_configs["gather"]["wait_ticks"] = datapack_configs['gather']['wait_seconds'] * datapack_configs['datapack']['ticks_per_second']

    if "enabled_regions" not in datapack_configs["gather"]:
        datapack_configs["gather"]["enabled_regions"] = list(region_configs.region_classes.keys())

    for region in datapack_configs["gather"]["enabled_regions"]:
        datapack_configs['regions'][region] = region_configs.region_classes[region]().get_config()

    return datapack_configs