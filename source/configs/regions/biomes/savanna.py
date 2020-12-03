from ..base_region import BaseRegion

class Savanna(BaseRegion):
    def __init__(self):
        self.name = 'savanna'
        self.display_name = 'Savanna'

        self.items = {
                'minecraft:oak_log': 0.5,
                'minecraft:acacia_log': 1,
                'minecraft:oak_sapling': 0.25,
                'minecraft:acacia_sapling': 0.5,
                'minecraft:stick': 0.5,
        }

        self.resources_by_tool = {}
        self.resources_by_tool['axe'] = {
            'default': {
                'minecraft:oak_log': 0.5,
                'minecraft:acacia_log': 1,
                'minecraft:oak_sapling': 0.25,
                'minecraft:acacia_sapling': 0.5,
                'minecraft:stick': 0.5,
            },
            'minecraft:silk_touch': {
                'minecraft:oak_leaves': 0.5,
                'minecraft:acacia_leaves': 1,
            }
        }

        self.resources_by_tool['hoe'] = {
            'default': {
                "minecraft:wheat_seeds": 1,
            }
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
                "minecraft:oak_leaves": 8,
                "minecraft:acacia_leaves": 8,
                "minecraft:grass": 2,
            }
        }
        
        self.resources_by_tool[self.fallback] = self.resources_by_tool['axe']