"""
Settings
=================================

This folder includes all of the settings for the datapack.
Settings are defined using either yaml or python classes.

For example, the :ref:`Global<settings-global>` settings are defined
using yaml, while the :ref:`Regions<settings-regions>` settings are in python classes.

.. autofunction:: fetch

----

.. toctree::
    :caption: Setting Categories
    :maxdepth: 1

    global
    gather
    scoreboards
    tools
    enchantments
    regions/index

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

# The fetched datapack settings are stored on this variable for easy lookup on the next fetch() run
_cached_datapack_settings = None

def fetch(yaml_only=False, prints_enabled=False):
    """Fetches and parses all of the settings for the datapack.
    This function is the only (reliable) way to access the datapack settings.

    Args:
        yaml_only (bool, optional): Only fetch the yaml settings files. Defaults to False.
        prints_enabled (bool, optional): Should the function output (pretty) print statements. Defaults to False.

    Returns:
        dict: The formatted datapack settings dict
    """
    global _cached_datapack_settings

    if _cached_datapack_settings is not None:
        return _cached_datapack_settings

    datapack_settings = {
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

    datapack_settings["global"] = helpers.read_yaml_file(os.path.join(config.SETTINGS_DIR, 'global.yaml'))
    datapack_settings["scoreboards"] = helpers.read_yaml_file(os.path.join(config.SETTINGS_DIR, 'scoreboards.yaml'))
    datapack_settings["gather"] = helpers.read_yaml_file(os.path.join(config.SETTINGS_DIR, 'gather.yaml'))

    # Calc how many ticks should we wait between each grind session
    datapack_settings["gather"]["wait_ticks"] = datapack_settings['gather']['wait_seconds'] * datapack_settings['global']['ticks_per_second']

    # If yaml_only then we can stop here.
    # This is intentionally not cached -- only the full settings dict will be cached.
    if yaml_only:
        return datapack_settings

    # Get the python module names for each region module
    region_module_names = [region for region, module in getmembers(region_configs, ismodule) if region != 'base_region']

    if prints_enabled:
        print(colored(f'Found {len(region_module_names)} Regions...', 'cyan'))
        print(f'{", ".join(region_module_names)}')
        print(colored('\nCreating Region Configs...', 'cyan'))

    # Stores the y axis where mines end
    mines_end_y = None

    # For each region
    #   generate it's config
    #   store the config in the overall datapack configs
    for region in region_module_names:
        if prints_enabled:
            status = colored(f'{region}')
            print(status, '...', end="\r")

        # Get the region python module. From the module get the region class (region class member)
        region_module = getattr(region_configs, region)
        region_classname = region.replace("_", "")
        region_class_member = list(filter(lambda module: module[0].lower() == region_classname.lower(), getmembers(region_module)))

        # Oh dear! We couldn't find a matching class in this region module.
        #   If this happens, check that the class name in the broken module is a pascal-case verison of the filename
        #   TODO: This should be a test!
        if len(region_class_member) == 0:
            if prints_enabled:
                print(colored(f'Error! No class found for', 'red', attrs=['bold']), status)
            continue

        # Create an instance of the region
        region_class = region_class_member[0][1]()
        region_type = region_class.region_type

        # Store the region name in a helper list (for easy looping later on)
        datapack_settings[f'{region_type}_regions'].append(region)

        # Store the region config (holds the items given and tools supported for the region)
        datapack_settings['regions'][region] = region_class.create_config()

        # If the region is an overworld mine, check to see where the mine ends (end_y)
        #   If it's higher up than what's stored save it to mines_ends_y
        if region_type == 'overworld_mine':
            y_range = region_class.y_range

            if mines_end_y is None:
                mines_end_y = y_range[1]
            else:
                mines_end_y = max(y_range[1], mines_end_y)

        if prints_enabled:
            print(colored(f'DONE', 'green', attrs=['bold']), status)

    # No mining is supported above this y value
    datapack_settings['mines_end_y'] = mines_end_y + 1

    # Cache all this mess so we don't generate it again
    _cached_datapack_settings = datapack_settings

    # aaaand we're done.
    return datapack_settings
