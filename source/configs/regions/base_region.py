import math
from pprint import pprint

class BaseRegion():
    name = 'base'
    display_name = 'Base'
    resources_by_tool = {}
    material_addons = {}

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

    multipliers = {
        'default': 8,
        'wooden': 16,
        'stone': 24,
        'iron': 32,
        'diamond': 36,
        'netherite': 40,
        'golden': 48
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
            tool_multiplier = self.multipliers['default']
        else:
            tool_multiplier = self.multipliers[material]
    
        tool_stanza = {}
        for subtype, gives in subtypes.items():
            tool_stanza[subtype] = {}

            if 'damage' in gives:
                tool_stanza[subtype]['damage'] = math.floor(gives['damage'] * tool_multiplier)

            if 'items' in gives:
                tool_stanza[subtype]['items'] = {}
                for item, amount in gives['items'].items():
                    tool_stanza[subtype]['items'][item] = math.floor(amount * tool_multiplier)

        return tool_key, tool_stanza