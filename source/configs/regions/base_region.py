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
            'default':  1/2,
            'wooden': 1/4,
            'stone': 1/6,
            'iron': 1/8,
            'diamond': 1/9,
            'netherite': 1/10,
            'golden': 1/11
        }
    }

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
            tool_stanza[subtype] = {}
            tool_stanza[subtype]['items'] = {}
            
            num_items_given = 0
            for item, amount in gives.items():
                num_items_given += amount
                tool_stanza[subtype]['items'][item] = math.floor(amount * material_multiplier)

            tool_stanza[subtype]['damage'] =  math.floor((material_multiplier * num_items_given) * damage_multiplier)
    
        if 'default' in tool_stanza:
            tool_stanza['minecraft:unbreaking'] = dict(**tool_stanza['default'])
            tool_stanza['minecraft:unbreaking']['damage'] = math.floor(tool_stanza['default']['damage'] / 2)

        return tool_key, tool_stanza