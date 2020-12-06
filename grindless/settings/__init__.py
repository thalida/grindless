"""
Settings
=================================

General configs for the data pack

.. autofunction:: fetch


.. raw:: html

   <h2>Regions</h2>

read more about :doc:`regions/index`.

.. toctree::
    :hidden:
    :maxdepth: 1

    regions/index

Global
-------------
global settings


Gather
--------------------
gather settings


Scoreboards
----------------------
scoreboard settings

"""

# Builtin
import os
from inspect import getmembers, ismodule
# Installed
import colorama 
from termcolor import colored
# Internal
from . import regions as region_configs
import grindless.config as config
import grindless.helpers as helpers


colorama.init()
cached_datapack_configs = None

def fetch(from_console=False):
    global cached_datapack_configs

    if cached_datapack_configs is not None:
        return cached_datapack_configs
    
    datapack_configs = {
        # These configs are pulled from yaml files
        "global": {},
        "scoreboards": {},
        "gather": {},

        # The below are generated from python files
        "regions": {},
        "overworld_regions": [],
        "overworld_mine_regions": [],
        "nether_regions": [],
        "end_regions": [],
        "mines_end_y": None,
    }

    datapack_configs["global"] = helpers.read_yaml_file(os.path.join(config.CONFIGS_DIR, 'global.yaml'))
    datapack_configs["scoreboards"] = helpers.read_yaml_file(os.path.join(config.CONFIGS_DIR, 'scoreboards.yaml'))
    datapack_configs["gather"] = helpers.read_yaml_file(os.path.join(config.CONFIGS_DIR, 'gather.yaml'))

    # Calc how many ticks should we wait between each grind session
    datapack_configs["gather"]["wait_ticks"] = datapack_configs['gather']['wait_seconds'] * datapack_configs['global']['ticks_per_second']
    
    # Get the python module names for each region module
    region_module_names = [region for region, module in getmembers(region_configs, ismodule) if region != 'base_region']

    if from_console:
        print(colored(f'Found {len(region_module_names)} Regions...', 'cyan'))
        print(f'{", ".join(region_module_names)}')
        print(colored('\nCreating Region Configs...', 'cyan'))

    # Stores the y axis where mines end
    mines_end_y = None

    # For each region
    #   generate it's config
    #   store the config in the overall datapack configs
    for region in region_module_names:
        status = colored(f'{region}')
        if from_console:
            print(status, '...', end="\r")
        
        # Get the region python module. From the module get the region class (region class member)
        region_module = getattr(region_configs, region)
        region_classname = region.replace("_", "")
        region_class_member = list(filter(lambda module: module[0].lower() == region_classname.lower(), getmembers(region_module)))

        # Oh dear! We couldn't find a matching class in this region module.
        #   If this happens, check that the class name in the broken module is a pascal-case verison of the filename
        #   TODO: This should be a test!
        if len(region_class_member) == 0:
            if from_console:
                print(colored(f'Error! No class found for', 'red', attrs=['bold']), status)
            continue
        
        # Create an instance of the region
        region_class = region_class_member[0][1]()
        region_type = region_class.region_type
        
        # Store the region name in a helper list (for easy looping later on)
        datapack_configs[f'{region_type}_regions'].append(region)
        
        # Store the region config (holds the items given and tools supported for the region)
        datapack_configs['regions'][region] = region_class.create_config()
        
        # If the region is an overworld mine, check to see where the mine ends (end_y)
        #   If it's higher up than what's stored save it to mines_ends_y
        if region_type == 'overworld_mine':
            y_range = region_class.y_range
            
            if mines_end_y is None:
                mines_end_y = y_range[1]
            else:
                mines_end_y = max(y_range[1], mines_end_y)
        
        if from_console:
            print(colored(f'DONE', 'green', attrs=['bold']), status)

    # No mining is supported above this y value
    datapack_configs['mines_end_y'] = mines_end_y + 1

    # Cache all this mess so we don't generate it again
    cached_datapack_configs = datapack_configs

    # aaaand we're done.
    return datapack_configs