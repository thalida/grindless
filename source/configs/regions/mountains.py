from .base_region import BaseRegion

class Mountains(BaseRegion):
    def __init__(self):
        self.name = 'mountains'
        self.display_name = 'Mountains'

        self.resources_by_tool = {}
        self.resources_by_tool['axe'] = {
            'default': {
                'minecraft:oak_log': 1,
                'minecraft:oak_sapling': 0.5,
                'minecraft:spruce_log': 1,
                'minecraft:spruce_sapling': 0.5,
            },
            'minecraft:silk_touch': {
                'minecraft:spruce_leaves': 1,
                'minecraft:oak_leaves': 1,
            }
        }

        self.resources_by_tool['pickaxe'] = {
            'default': {
                "minecraft:cobblestone": 1,
            },
            'minecraft:silk_touch': {
                "minecraft:stone": 1,
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
                "minecraft:snowball": 0.5,
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
                "minecraft:spruce_leaves": 4,
                "minecraft:oak_leaves": 4,
                "minecraft:grass": 2,
            }
        }
        
        self.resources_by_tool[self.fallback] = {
            'default': {
                'minecraft:spruce_log': 1,
                'minecraft:spruce_sapling': 0.3,
                'minecraft:oak_log': 1,
                'minecraft:oak_sapling': 0.3,
                "minecraft:snowball": 0.5,
            },
            'minecraft:silk_touch': {
                'minecraft:spruce_leaves': 1,
                'minecraft:oak_leaves': 1,
            }
        }