import os
import yaml
import pathlib
from inspect import getmembers, ismodule

import config
import source.configs.regions as region_configs

def read_yaml_file(filename):
    with open(filename, 'r') as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)

def get_region_config(region):
    region_module = getattr(region_configs, region)
    region_classname = region.replace("_", "")
    region_class_member = list(filter(lambda module: module[0].lower() == region_classname.lower(), getmembers(region_module)))
    
    if len(region_class_member) == 0:
        return None

    region_class = region_class_member[0][1]
    region_config = region_class().get_config()

    return region_config

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
        datapack_configs["gather"]["enabled_regions"] = [module_name for module_name, module in getmembers(region_configs, ismodule) if module_name != 'os' and module_name != 'base_region']

    for region in datapack_configs["gather"]["enabled_regions"]:
        region_module = getattr(region_configs, region)
        region_classname = region.replace("_", "")
        region_class_member = list(filter(lambda module: module[0].lower() == region_classname.lower(), getmembers(region_module)))
        
        if len(region_class_member) == 0:
            continue

        region_class = region_class_member[0][1]
        datapack_configs['regions'][region] = region_class().get_config()

    return datapack_configs