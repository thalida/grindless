"""
.. _settings-regions-baseregion:

BaseRegion
=============================
General configs for the data pack

.. autoclass:: grindless.settings.regions.base_region.BaseRegion
   :members:
   :undoc-members:
"""

import os
import math
import itertools
from copy import deepcopy
from pprint import pprint

from ... import helpers as helpers
from ... import config

class BaseRegion():
    name = 'base'
    display_name = 'Base'
    region_type = 'overworld' #overworld,end,nether,overworld_mine
    y_range = None
    items = {}

    def create_tool_key(self, tool, material=None):
        if tool == helpers.TOOL_SELECTORS['ANY']:
            return tool

        if material is None or len(material) == 0:
            return f'minecraft:{tool}'

        return f'minecraft:{material}_{tool}'


    def create_config(self):
        region_config = {
            'id': self.name,
            'display_name': self.display_name,
            'region_type': self.region_type,
            'y_range': self.y_range,
            'resources': {},
            'supported_tools': [],
        }

        items_config = helpers.read_yaml_file(os.path.join(config.REGIONS_DIR, 'items.yaml'))
        tools_config = helpers.read_yaml_file(os.path.join(config.SETTINGS_DIR, 'tools.yaml'))
        enchantments_config = helpers.read_yaml_file(os.path.join(config.SETTINGS_DIR, 'enchantments.yaml'))

        for item, region_multiplier in self.items.items():
            item_config = items_config[item]

            for tool, subtypes in item_config.items():
                if tool == helpers.TOOL_SELECTORS['ANY'] or tool in tools_config['tools_without_material']:
                    tool_type = tool
                    tool_materials = [None]
                else:
                    tool_material = None
                    for material in tools_config['supported_materials']:
                        if tool.find(material) >= 0:
                            tool_material = material
                            break

                    if tool_material is not None:
                        tool_type = tool.replace(f'{tool_material}_', '')
                        tool_materials = [tool_material]
                    else:
                        tool_type = tool
                        tool_materials = tools_config['supported_materials']

                if tool_type not in tools_config['supported_tool_types']:
                    # TODO: THROW ERROR
                    continue

                for material in tool_materials:
                    tool_key = self.create_tool_key(tool_type, material=material)

                    if material is None:
                        material_multiplier = tools_config['item_multipliers_by_material']['default']
                    else:
                        material_multiplier = tools_config['item_multipliers_by_material'][material]

                    for subtype, gives in subtypes.items():
                        if not enchantments_config['enabled'] and subtype in enchantments_config['supported_enchantments']:
                            continue

                        if subtype not in enchantments_config['supported_enchantments'] and subtype != 'default':
                            # TODO: THROW ERROR
                            continue

                        item_amount = math.ceil(gives * region_multiplier * material_multiplier)

                        if item_amount <= 0:
                            continue

                        if tool_key not in region_config['resources']:
                            region_config['resources'][tool_key] = {}

                        if subtype not in region_config['resources'][tool_key]:
                            region_config['resources'][tool_key][subtype] = {
                                'tool_type': tool_type,
                                'tool_material': material,
                                'items': {}
                            }

                        region_config['resources'][tool_key][subtype]['items'][item] = item_amount

                        if not enchantments_config['enabled']:
                            continue

                        found_enchantments = []
                        for enchantment in sorted(enchantments_config['item_multipliers_by_enchantment'].keys()):
                            enchantment_key = f'{subtype}/minecraft:{enchantment}'
                            enchantment_multiplier = enchantments_config['item_multipliers_by_enchantment'][enchantment]

                            if enchantment not in enchantments_config['supported_enchantments_by_tool'].get(tool_type, []):
                                continue

                            if enchantment_key not in region_config['resources'][tool_key]:
                                region_config['resources'][tool_key][enchantment_key] = {
                                    'tool_type': tool_type,
                                    'tool_material': material,
                                    'items': {}
                                }

                            region_config['resources'][tool_key][enchantment_key]['items'][item] = math.ceil(item_amount * enchantment_multiplier)
                            found_enchantments.append(enchantment)

                        enchantment_combos = itertools.combinations(found_enchantments, len(found_enchantments))
                        for enchantment_combo in enchantment_combos:
                            if len(enchantment_combo) <= 1:
                                continue

                            enchantments = list(enchantment_combo)
                            enchantments.sort()
                            combo_key = '&minecraft:'.join(enchantments)
                            combo_key = f'{subtype}/minecraft:{combo_key}'
                            combo_multiplier = 1

                            for enchantment in enchantments:
                                combo_multiplier *= enchantments_config['item_multipliers_by_enchantment'][enchantment]

                            if combo_key not in region_config['resources'][tool_key]:
                                region_config['resources'][tool_key][combo_key] = {
                                    'tool_type': tool_type,
                                    'tool_material': material,
                                    'items': {}
                                }

                            region_config['resources'][tool_key][combo_key]['items'][item] = math.ceil(item_amount * combo_multiplier)

        resources_copy = deepcopy(region_config['resources'])
        for tool_key, tool_stanza in resources_copy.items():
            for subtype, subtype_stanza in tool_stanza.items():
                material = subtype_stanza['tool_material']
                tool_type = subtype_stanza['tool_type']
                num_items_given = sum(subtype_stanza['items'].values())

                if material is None:
                    damage_multiplier = tools_config['damage_multipliers_by_material']['default']
                else:
                    damage_multiplier = tools_config['damage_multipliers_by_material'][material]

                damage = math.floor(num_items_given * damage_multiplier)
                region_config['resources'][tool_key][subtype]['damage'] = damage

                if not enchantments_config['enabled']:
                    continue

                for enchantment in sorted(enchantments_config['damage_multipliers_by_enchantment'].keys()):
                    if enchantment not in enchantments_config['supported_enchantments_by_tool'].get(tool_type, []):
                        continue

                    if enchantment in enchantments_config['item_multipliers_by_enchantment']:
                        continue

                    if subtype.find('/') < 0:
                        enchantment_key = f'{subtype}/minecraft:{enchantment}'
                    else:
                        enchantment_key = f'{subtype}&minecraft:{enchantment}'

                    enchantment_multiplier = enchantments_config['damage_multipliers_by_enchantment'][enchantment]
                    enchantment_damage = math.floor(damage * enchantment_multiplier)

                    region_config['resources'][tool_key][enchantment_key] = deepcopy(subtype_stanza)
                    region_config['resources'][tool_key][enchantment_key]['damage'] = enchantment_damage

        region_config["supported_tools"] = [tool for tool in region_config["resources"].keys() if tool != helpers.TOOL_SELECTORS['ANY']]
        return region_config
