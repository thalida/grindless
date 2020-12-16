"""
.. _settings-regions-baseregion:

BaseRegion
=============================
The base class extended by all regions.

.. autoclass:: grindless.settings.regions.base_region.BaseRegion
   :members:
   :undoc-members:

"""

import os
import math
import itertools
from copy import deepcopy
from pprint import pprint
from abc import ABCMeta, abstractmethod

from ... import helpers as helpers
from ... import config

#: Imports the items settings
items_config = helpers.read_yaml_file(os.path.join(config.REGIONS_DIR, 'items.yaml'))
# Imports the tool settings
tools_config = helpers.read_yaml_file(os.path.join(config.SETTINGS_DIR, 'tools.yaml'))
# Imports the enchantment settings
enchantments_config = helpers.read_yaml_file(os.path.join(config.SETTINGS_DIR, 'enchantments.yaml'))

class BaseRegion():
    __metaclass__ = ABCMeta

    def __init__(self):
        #: Region namespace
        self.name = 'base'
        #: Human-readable name
        self.display_name = 'Base'
        #: Defines the group the region is in
        #: Defaults to 'overworld'.
        #: Supported options are: end, nether, overworld, overworld_mine
        self.region_type = 'overworld'
        #: y-axis range the region is contained by (only used for mines)
        self.y_range = None
        #: Houses the items given by the region
        self.items = {}

        self.setup_region()

        self.config = self.create_config()

    @abstractmethod
    def setup_region(self):
        raise NotImplementedError("Must override methodB")

    def create_config(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        region_config = {
            'id': self.name,
            'display_name': self.display_name,
            'region_type': self.region_type,
            'y_range': self.y_range,
            'resources': {},
            'supported_tools': [],
        }

        for item, region_multiplier in self.items.items():
            for tool, options in items_config[item].items():
                tool_type, supported_materials = self.get_tool_info(tool)

                if tool_type not in tools_config['supported_tool_types']:
                    # TODO: THROW ERROR
                    continue

                for opt, item_multiplier in options.items():
                    if not enchantments_config['enabled'] and opt in enchantments_config['supported_enchantments']:
                        continue

                    if opt not in enchantments_config['supported_enchantments'] and opt != 'default':
                        # TODO: THROW ERROR
                        continue

                    for tool_material in supported_materials:
                        tool_key = self.create_tool_key(tool_type, tool_material=tool_material)
                        give_amount = self.get_give_amount(item_multiplier, region_multiplier, tool_material=tool_material)

                        if give_amount <= 0:
                            continue

                        if tool_key not in region_config['resources']:
                            region_config['resources'][tool_key] = {}

                        if opt not in region_config['resources'][tool_key]:
                            region_config['resources'][tool_key][opt] = {
                                'tool_type': tool_type,
                                'tool_material': tool_material,
                                'items': {}
                            }

                        region_config['resources'][tool_key][opt]['items'][item] = give_amount

                        if not enchantments_config['enabled']:
                            continue

                        enchantment_drops = self.create_enchantment_drops_configs(opt, give_amount)
                        for enchantment_key, item_amount in enchantment_drops.items():
                            if enchantment_key not in region_config['resources'][tool_key]:
                                region_config['resources'][tool_key][enchantment_key] = {
                                    'tool_type': tool_type,
                                    'tool_material': tool_material,
                                    'items': {}
                                }

                            region_config['resources'][tool_key][enchantment_key]['items'][item] = item_amount


        resources_copy = deepcopy(region_config['resources'])
        for tool_key, tool_stanza in resources_copy.items():
            for tool_option, condition_stanza in tool_stanza.items():
                material = condition_stanza['tool_material']
                tool_type = condition_stanza['tool_type']

                damage = self.get_damage_amount(condition_stanza['items'], tool_material)
                region_config['resources'][tool_key][tool_option]['damage'] = damage

                if not enchantments_config['enabled']:
                    continue

                enchantment_damage_configs = self.create_enchantment_damage_configs(tool_type, tool_option, damage)
                for enchantment_key, enchantment_damage in enchantment_damage_configs.items():
                    region_config['resources'][tool_key][enchantment_key] = deepcopy(condition_stanza)
                    region_config['resources'][tool_key][enchantment_key]['damage'] = enchantment_damage

        region_config["supported_tools"] = [tool for tool in region_config["resources"].keys() if tool != helpers.TOOL_SELECTORS['ANY']]
        return region_config


    @staticmethod
    def create_tool_key(tool, tool_material=None):
        """[summary]

        Args:
            tool ([type]): [description]
            material ([type], optional): [description]. Defaults to None.

        Returns:
            [type]: [description]
        """
        if tool == helpers.TOOL_SELECTORS['ANY']:
            return tool

        if tool_material is None or len(tool_material) == 0:
            return f'minecraft:{tool}'

        return f'minecraft:{tool_material}_{tool}'

    @staticmethod
    def get_tool_info(tool):
        """[summary]

        Args:
            tool ([type]): [description]

        Returns:
            [type]: [description]
        """
        if tool == helpers.TOOL_SELECTORS['ANY'] or tool in tools_config['tools_without_material']:
            tool_type = tool
            supported_materials = [None]
            return tool_type, supported_materials

        tool_material = None
        for material in tools_config['supported_materials']:
            if tool.find(material) >= 0:
                tool_material = material
                break

        if tool_material is not None:
            tool_type = tool.replace(f'{tool_material}_', '')
            supported_materials = [tool_material]
            return tool_type, supported_materials

        tool_type = tool
        supported_materials = tools_config['supported_materials']
        return tool_type, supported_materials


    @staticmethod
    def get_give_amount(item_multiplier, region_multiplier, tool_material=None):
        """[summary]

        Args:
            item_multiplier ([type]): [description]
            region_multiplier ([type]): [description]
            tool_material ([type], optional): [description]. Defaults to None.

        Returns:
            [type]: [description]
        """
        if tool_material is None:
            material_multiplier = tools_config['item_multipliers_by_material']['default']
        else:
            material_multiplier = tools_config['item_multipliers_by_material'][tool_material]

        give_amount = math.ceil(item_multiplier * region_multiplier * material_multiplier)

        return give_amount

    @staticmethod
    def get_damage_amount(items, tool_material):
        """[summary]

        Args:
            items ([type]): [description]
            tool_material ([type]): [description]

        Returns:
            [type]: [description]
        """
        num_items_given = sum(items.values())

        if tool_material is None:
            damage_multiplier = tools_config['damage_multipliers_by_material']['default']
        else:
            damage_multiplier = tools_config['damage_multipliers_by_material'][tool_material]

        damage = math.floor(num_items_given * damage_multiplier)

        return damage

    @staticmethod
    def create_enchantment_drops_configs(tool_option, give_amount):
        """[summary]

        Args:
            tool_option ([type]): [description]
            give_amount ([type]): [description]

        Returns:
            [type]: [description]
        """
        enchantment_drops_configs = {}

        enchantment_item_multi_combos = []
        item_multi_keys = enchantments_config['item_multipliers_by_enchantment'].keys()
        for size in range(1, len(item_multi_keys) + 1):
            combos = itertools.combinations(item_multi_keys, size)
            enchantment_item_multi_combos += combos

        for enchantments in enchantment_item_multi_combos:
            enchantment_keys = '&minecraft:'.join(enchantments)
            enchantment_key = f'{tool_option}/minecraft:{enchantment_keys}'

            enchantment_multiplier = 1
            for enchantment in enchantments:
                enchantment_multiplier *= enchantments_config['item_multipliers_by_enchantment'][enchantment]
                enchantment_drops_configs[enchantment_key] = math.ceil(give_amount * enchantment_multiplier)

        return enchantment_drops_configs


    @staticmethod
    def create_enchantment_damage_configs(tool_type, tool_option, damage_amount):
        """[summary]

        Args:
            tool_type ([type]): [description]
            tool_option ([type]): [description]
            damage_amount ([type]): [description]

        Returns:
            [type]: [description]
        """
        enchantment_damage_configs = {}
        for enchantment in sorted(enchantments_config['damage_multipliers_by_enchantment'].keys()):
            if enchantment not in enchantments_config['supported_enchantments_by_tool'].get(tool_type, []):
                continue

            if enchantment in enchantments_config['item_multipliers_by_enchantment']:
                continue

            if tool_option.find('/') < 0:
                enchantment_key = f'{tool_option}/minecraft:{enchantment}'
            else:
                enchantment_key = f'{tool_option}&minecraft:{enchantment}'

            enchantment_multiplier = enchantments_config['damage_multipliers_by_enchantment'][enchantment]
            enchantment_damage = math.floor(damage_amount * enchantment_multiplier)

            enchantment_damage_configs[enchantment_key] = enchantment_damage

        return enchantment_damage_configs
