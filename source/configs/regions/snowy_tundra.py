from .base_region import BaseRegion

class SnowyTundra(BaseRegion):
    def __init__(self):
        self.name = 'snowy_tundra'
        self.display_name = 'Snowy Tundra'

        self.resources_by_tool = {}
        self.resources_by_tool['axe'] = {
            'default': {
                'minecraft:spruce_log': 1.25,
                'minecraft:spruce_sapling': 0.5,
            },
            'minecraft:silk_touch': {
                'minecraft:spruce_leaves': 1,
            }
        }
        
        self.resources_by_tool['pickaxe'] = {
            'minecraft:silk_touch': {
                'minecraft:ice': 1,
            }
        }

        self.resources_by_tool['hoe'] = {
            'default': {
                "minecraft:wheat_seeds": 0.5,
            }
        }

        self.resources_by_tool['shovel'] = {
            'default': {
                "minecraft:dirt": 1,
                "minecraft:snow_ball": 1,
                "minecraft:wheat_seeds": 0.2,
            },
            'minecraft:silk_touch': {
                "minecraft:snow": 1,
                "minecraft:grass_block": 0.5,
                "minecraft:wheat_seeds": 0.2,
            }
        }

        self.resources_by_tool['shears'] = {
            'default': {
                "minecraft:spruce_leaves": 8,
                "minecraft:grass": 2,
            }
        }
        
        self.resources_by_tool[self.fallback] = {
            'default': {
                'minecraft:spruce_log': 1,
                'minecraft:spruce_sapling': 0.3,
                "minecraft:snow_ball": 0.5,
            },
            'minecraft:silk_touch': {
                'minecraft:spruce_leaves': 1,
            }
        }