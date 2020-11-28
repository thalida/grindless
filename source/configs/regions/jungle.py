from .base_region import BaseRegion

class Jungle(BaseRegion):
    def __init__(self):
        self.name = 'jungle'
        self.display_name = 'Jungle'

        self.resources_by_tool = {}
        self.resources_by_tool['axe'] = {
            'default': {
                'minecraft:jungle_log': 2,
                'minecraft:jungle_sapling': 1,
                'minecraft:cocoa_beans': 0.4,
                'minecraft:bamboo': 0.25,
                'minecraft:melon_slice': 0.25,
            },
            'minecraft:silk_touch': {
                'minecraft:jungle_leaves': 2,
                'minecraft:melon': 0.25,
            }
        }

        self.resources_by_tool['sword'] = {
            'default': {
                "minecraft:bamboo": 1,
            },
        }

        self.resources_by_tool['shovel'] = {
            'default': {
                "minecraft:dirt": 1,
                "minecraft:wheat_seeds": 0.25,
            },
            'minecraft:silk_touch': {
                "minecraft:grass_block": 1,
                "minecraft:wheat_seeds": 0.25,
            }
        }

        self.resources_by_tool['shears'] = {
            'default': {
                "minecraft:vine": 2,
                "minecraft:jungle_leaves": 2,
            }
        }
        
        self.resources_by_tool[self.fallback] = self.resources_by_tool['axe']