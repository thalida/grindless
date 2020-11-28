import math
from pprint import pprint

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
        'fortune_looting_damage': -0.2
    }

    tool_subtypes = [
        'default', 
        'minecraft:unbreaking',
        'minecraft:efficiency',
        'minecraft:fortune',
        'minecraft:silk_touch',
        'minecraft:luck_of_the_sea',
        'minecraft:lure'
    ]

    def __init__(self):
        pass

    def get_config(self):
        config = {
            'id': self.name,
            'display_name': self.display_name,
            'resources': {},
            'supported_tools': [],
        }

        for tool, subtypes in self.resources_by_tool.items():
            if tool == self.fallback or tool in self.tools_without_material:
                tool_key, tool_stanza = self.get_tool_stanza(tool, subtypes)
                config['resources'][tool_key] = tool_stanza
                continue
            
            if tool not in self.tools_without_material:
                for material in self.tool_materials:
                    tool_key, tool_stanza = self.get_tool_stanza(tool, subtypes, material=material)
                    config['resources'][tool_key] = tool_stanza
        
        config["supported_tools"] = [tool for tool in config["resources"].keys() if tool != self.fallback]
        return config

    def is_valid_subtype(self, subtype): 
        return subtype in self.tool_subtypes
    
    def get_tool_stanza(self, tool, subtypes, material=None):
        tool_stanza = {}

        if tool == self.fallback:
            tool_key = tool
        elif tool in self.tools_without_material:
            tool_key = f"minecraft:{tool}"
        elif material is not None:
            tool_key = f"minecraft:{material}_{tool}"

        if material is None:
            material_multiplier = self.material_multipliers['items']['default']
            damage_multiplier = self.material_multipliers['damage']['default']
        else:
            material_multiplier = self.material_multipliers['items'][material]
            damage_multiplier = self.material_multipliers['damage'][material]
    
        for subtype, gives in subtypes.items():
            if not self.is_valid_subtype(subtype):
                print('Found invalid subtype', subtype)
                continue

            tool_stanza[subtype] = {}
            tool_stanza[subtype]['items'] = {}
            
            num_items_given = 0
            for item, amount in gives.items():
                num_items_given += amount
                tool_stanza[subtype]['items'][item] = math.floor(amount * material_multiplier)

            if subtype == 'minecraft:fortune' or subtype == 'minecraft:looting':
                damage_multiplier += self.material_multipliers['fortune_looting_damage']

            damage = math.floor((material_multiplier * num_items_given) * damage_multiplier)
            tool_stanza[subtype]['damage'] = damage
    
        clone_unbreaking_from = None
        if 'minecraft:fortune' in tool_stanza:
            clone_unbreaking_from = 'minecraft:fortune'
        elif 'minecraft:looting' in tool_stanza:
            clone_unbreaking_from = 'minecraft:looting'
        elif 'default' in tool_stanza:
            clone_unbreaking_from = 'default'
        
        if 'minecraft:unbreaking' in tool_stanza:
            source_stanza = tool_stanza[clone_unbreaking_from]
            tool_stanza['minecraft:unbreaking'] = dict(**source_stanza)
            tool_stanza['minecraft:unbreaking']['damage'] = math.floor(source_stanza['damage'] / 2)

        return tool_key, tool_stanza