import os
import math
import itertools
from copy import deepcopy
from pprint import pprint

import helpers
import config

class BaseRegion():
    name = 'base'
    display_name = 'Base'
    resources_by_tool = {}
    material_addons = {}

    always = 'always'
    fallback = '0+'

    tool_materials = [
        'wooden',
        'stone',
        'iron',
        'diamond',
        'netherite',
        'golden',
    ]

    tools_without_material = ['shears', 'fishing_rod']

    material_multipliers = {
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
            'default':  .5,
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

    tool_addon_enchantments = [
        'unbreaking',
        'efficiency',
        'fortune',
    ]

    enchantment_multipliers = {
        'items': {
            'efficiency': 1.2,
            'fortune': 1.4,
        },
        'damage': {
            'unbreaking': 0.5,
            'efficiency': 0.8,
        }
    }

    enchantments_by_tool = {
        'axe': ['unbreaking', 'efficiency', 'fortune'],
        'pickaxe': ['unbreaking', 'efficiency', 'fortune'],
        'shovel': ['unbreaking', 'efficiency', 'fortune'],
        'hoe': ['unbreaking', 'efficiency', 'fortune'],
        'shears': ['unbreaking', 'efficiency'],
        'fishing_rod': ['unbreaking']
    }

    def __init__(self):
        pass
    
    def create_tool_key(self, tool, material=None):
        if tool == self.fallback:
            return tool

        if material is None or len(material) == 0:
            return f'minecraft:{tool}'

        return f'minecraft:{material}_{tool}'

    
    def create_config(self):
        region_config = {
            'id': self.name,
            'display_name': self.display_name,
            'resources': {},
            'supported_tools': [],
        }
        
        items_config = helpers.read_yaml_file(os.path.join(config.CONFIGS_DIR, 'items.yaml'))

        for item, region_multiplier in self.items.items():
            item_config = items_config[item]

            for tool, subtypes in item_config.items():
                if tool == self.fallback or tool in self.tools_without_material:
                    tool_materials = [None]
                else:
                    tool_materials = self.tool_materials

                for material in tool_materials:
                    tool_key = self.create_tool_key(tool, material=material)
                    
                    if material is None:
                        material_multiplier = self.material_multipliers['items']['default']
                    else:
                        material_multiplier = self.material_multipliers['items'][material]

                    if tool_key not in region_config['resources']:
                        region_config['resources'][tool_key] = {}
                    
                    for subtype, gives in subtypes.items():
                        if subtype not in region_config['resources'][tool_key]:
                            region_config['resources'][tool_key][subtype] = {
                                'tool_type': tool,
                                'tool_material': material,
                                'items': {}
                            }

                        item_amount = math.ceil(gives * region_multiplier * material_multiplier)
                        region_config['resources'][tool_key][subtype]['items'][item] = item_amount

                        found_enchantments = []
                        for enchantment in sorted(self.enchantment_multipliers['items'].keys()):
                            enchantment_key = f'{subtype}/minecraft:{enchantment}'
                            enchantment_multiplier = self.enchantment_multipliers['items'][enchantment]

                            if enchantment not in self.enchantments_by_tool.get(tool, []):
                                continue
                            
                            if enchantment_key not in region_config['resources'][tool_key]:
                                region_config['resources'][tool_key][enchantment_key] = {
                                    'tool_type': tool,
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
                                combo_multiplier *= self.enchantment_multipliers['items'][enchantment]
                            
                            if combo_key not in region_config['resources'][tool_key]:
                                region_config['resources'][tool_key][combo_key] = {
                                    'tool_type': tool,
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
                    damage_multiplier = self.material_multipliers['damage']['default']
                else:
                    damage_multiplier = self.material_multipliers['damage'][material]

                damage = math.floor(num_items_given * damage_multiplier)
                region_config['resources'][tool_key][subtype]['damage'] = damage
                
                for enchantment in sorted(self.enchantment_multipliers['damage'].keys()): 
                    if enchantment not in self.enchantments_by_tool.get(tool_type, []):
                        continue

                    if enchantment in self.enchantment_multipliers['items']:
                        continue
                    
                    if subtype.find('/') < 0:
                        enchantment_key = f'{subtype}/minecraft:{enchantment}'
                    else:
                        enchantment_key = f'{subtype}&minecraft:{enchantment}'
                    
                    enchantment_multiplier = self.enchantment_multipliers['damage'][enchantment]
                    enchantment_damage = math.floor(damage * enchantment_multiplier)

                    region_config['resources'][tool_key][enchantment_key] = deepcopy(subtype_stanza)
                    region_config['resources'][tool_key][enchantment_key]['damage'] = enchantment_damage

        region_config["supported_tools"] = [tool for tool in region_config["resources"].keys() if tool != self.fallback]
        return region_config
