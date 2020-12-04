import os
import yaml
import pathlib
from inspect import getmembers, ismodule

import colorama 
from termcolor import colored

colorama.init()

import config
import source.configs.regions as region_configs

cached_datapack_configs = None

def read_yaml_file(filename):
    with open(filename, 'r') as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)

def get_datapack_configs(from_console=False):
    global cached_datapack_configs

    if cached_datapack_configs is not None:
        return cached_datapack_configs
    
    datapack_configs = {
        "datapack": {},
        "scoreboards": {},
        "gather": {},
        "regions": {},
        "biome_regions": [],
        "mine_regions": [],
        "mines_end_y": None,
    }

    datapack_configs["datapack"] = read_yaml_file(os.path.join(config.CONFIGS_DIR, 'datapack.yaml'))
    datapack_configs["scoreboards"] = read_yaml_file(os.path.join(config.CONFIGS_DIR, 'scoreboards.yaml'))
    datapack_configs["gather"] = read_yaml_file(os.path.join(config.CONFIGS_DIR, 'gather.yaml'))
    datapack_configs["gather"]["wait_ticks"] = datapack_configs['gather']['wait_seconds'] * datapack_configs['datapack']['ticks_per_second']
    
    region_module_names = [region for region, module in getmembers(region_configs, ismodule) if region != 'base_region']

    if from_console:
        print(colored(f'Found {len(region_module_names)} Regions...', 'cyan'))
        print(f'{", ".join(region_module_names)}')
        print(colored('\nCreating Region Configs...', 'cyan'))

    mines_end_y = None
    for region in region_module_names:
        status = colored(f'{region}')
        if from_console:
            print(status, '...', end="\r")
            
        region_module = getattr(region_configs, region)
        region_classname = region.replace("_", "")
        region_class_member = list(filter(lambda module: module[0].lower() == region_classname.lower(), getmembers(region_module)))

        if len(region_class_member) == 0:
            if from_console:
                print(colored(f'Error! No class found for', 'red', attrs=['bold']), status)
            continue

        region_class = region_class_member[0][1]()
        region_type = region_class.region_type
        
        datapack_configs[f'{region_type}_regions'].append(region)
        datapack_configs['regions'][region] = region_class.create_config()

        if region_type == 'mine':
            y_range = region_class.y_range
            
            if mines_end_y is None:
                mines_end_y = y_range[1]
            else:
                mines_end_y = max(y_range[1], mines_end_y)
        
        if from_console:
            print(colored(f'DONE', 'green', attrs=['bold']), status)

    datapack_configs['mines_end_y'] = mines_end_y + 1

    cached_datapack_configs = datapack_configs
    return datapack_configs