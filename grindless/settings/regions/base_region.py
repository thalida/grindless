"""
Base Region
=============================
General configs for the data pack
"""

import os
import math
import itertools
from copy import deepcopy
from pprint import pprint

from ... import helpers as helpers
from ... import config

class BaseRegion():
    """base Region

    Returns:
        [type]: [description]
    """
    name = 'base'
    display_name = 'Base'
    region_type = 'overworld' #overworld,end,nether,overworld_mine
    y_range = None
    items = {}

    FALLBACK_SELECTOR = '0+'
    SUPPORED_MATERIALS = [
        'wooden',
        'stone',
        'iron',
        'diamond',
        'netherite',
        'golden',
    ]
    SIMPLE_TOOLS = ['shears', 'fishing_rod']
    MATERIAL_MULTIPLIERS = {
        'items': {
            'default': 8,
            'wooden': 16,
            'stone': 24,
            'iron': 32,
            'diamond': 36,
            'netherite': 40,
            'golden': 48
        },
        'damage': {
            'default': .5,
            'wooden': .25,
            'stone': .15,
            'iron': .125,
            'diamond': .1,
            'netherite': .09,
            'golden': .08
        },
        'fortune_looting_damage': .8,
        'unbreaking_damage': .5,
    }
    ENABLE_ENCHANTMENTS = True
    ENCHANTMENT_MULTIPLIERS = {
        'items': {
            'efficiency': 1.2,
            'fortune': 1.4,
        },
        'damage': {
            'unbreaking': 0.5,
            'efficiency': 0.8,
        }
    }
    SUPPORTED_ENCHANTMENTS = {
        'axe': ['unbreaking', 'efficiency', 'fortune'],
        'pickaxe': ['unbreaking', 'efficiency', 'fortune'],
        'shovel': ['unbreaking', 'efficiency', 'fortune'],
        'hoe': ['unbreaking', 'efficiency', 'fortune'],
        'shears': ['unbreaking', 'efficiency'],
        'fishing_rod': ['unbreaking']
    }
    
    def create_tool_key(self, tool, material=None):
        if tool == self.FALLBACK_SELECTOR:
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

        for item, region_multiplier in self.items.items():
            item_config = items_config[item]

            for tool, subtypes in item_config.items():
                if tool == self.FALLBACK_SELECTOR or tool in self.SIMPLE_TOOLS:
                    tool_type = tool
                    tool_materials = [None]
                else:
                    tool_material = None
                    for material in self.SUPPORED_MATERIALS:
                        if tool.find(material) >= 0:
                            tool_material = material
                            break
                    
                    if tool_material is not None:
                        tool_type = tool.replace(f'{tool_material}_', '')
                        tool_materials = [tool_material]
                    else:
                        tool_type = tool
                        tool_materials = self.SUPPORED_MATERIALS

                for material in tool_materials:
                    tool_key = self.create_tool_key(tool_type, material=material)
                    
                    if material is None:
                        material_multiplier = self.MATERIAL_MULTIPLIERS['items']['default']
                    else:
                        material_multiplier = self.MATERIAL_MULTIPLIERS['items'][material]
                    
                    for subtype, gives in subtypes.items():
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

                        if not self.ENABLE_ENCHANTMENTS:
                            continue

                        found_enchantments = []
                        for enchantment in sorted(self.ENCHANTMENT_MULTIPLIERS['items'].keys()):
                            enchantment_key = f'{subtype}/minecraft:{enchantment}'
                            enchantment_multiplier = self.ENCHANTMENT_MULTIPLIERS['items'][enchantment]

                            if enchantment not in self.SUPPORTED_ENCHANTMENTS.get(tool_type, []):
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
                                combo_multiplier *= self.ENCHANTMENT_MULTIPLIERS['items'][enchantment]
                            
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
                    damage_multiplier = self.MATERIAL_MULTIPLIERS['damage']['default']
                else:
                    damage_multiplier = self.MATERIAL_MULTIPLIERS['damage'][material]

                damage = math.floor(num_items_given * damage_multiplier)
                region_config['resources'][tool_key][subtype]['damage'] = damage

                if not self.ENABLE_ENCHANTMENTS:
                    continue
                
                for enchantment in sorted(self.ENCHANTMENT_MULTIPLIERS['damage'].keys()): 
                    if enchantment not in self.SUPPORTED_ENCHANTMENTS.get(tool_type, []):
                        continue

                    if enchantment in self.ENCHANTMENT_MULTIPLIERS['items']:
                        continue
                    
                    if subtype.find('/') < 0:
                        enchantment_key = f'{subtype}/minecraft:{enchantment}'
                    else:
                        enchantment_key = f'{subtype}&minecraft:{enchantment}'
                    
                    enchantment_multiplier = self.ENCHANTMENT_MULTIPLIERS['damage'][enchantment]
                    enchantment_damage = math.floor(damage * enchantment_multiplier)

                    region_config['resources'][tool_key][enchantment_key] = deepcopy(subtype_stanza)
                    region_config['resources'][tool_key][enchantment_key]['damage'] = enchantment_damage

        region_config["supported_tools"] = [tool for tool in region_config["resources"].keys() if tool != self.FALLBACK_SELECTOR]
        return region_config
