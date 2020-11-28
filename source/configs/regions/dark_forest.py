from .base_region import BaseRegion

class DarkForest(BaseRegion):
    def __init__(self):
        self.name = 'dark_forest'
        self.display_name = 'Dark Forest'

        self.resources_by_tool = {}
        self.resources_by_tool['axe'] = {
            'default': {
                'minecraft:dark_oak_log': 1,
                'minecraft:dark_oak_sapling': 0.5,
                'minecraft:apple': 0.2,
            },
            'minecraft:silk_touch': {
                'minecraft:dark_oak_leaves': 1,
                'minecraft:brown_mushroom_block': 0.2,
                'minecraft:red_mushroom_block': 0.2,
                'minecraft:mushroom_stem': 0.2,
            }
        }

        self.resources_by_tool['hoe'] = {
            'default': {
                'minecraft:red_mushroom': 0.2,
                'minecraft:brown_mushroom': 0.2,
                "minecraft:wheat_seeds": 1,
                "minecraft:dandelion": 0.5,
                "minecraft:poppy": 0.5,
                "minecraft:rose_bush": 0.25,
                "minecraft:lilac": 0.25,
                "minecraft:peony": 0.25,
                "minecraft:lily_of_the_valley": 0.25,
            },
            'minecraft:silk_touch': {
                'minecraft:brown_mushroom_block': 0.2,
                'minecraft:red_mushroom_block': 0.2,
                'minecraft:mushroom_stem': 0.2,
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
                "minecraft:dark_oak_leaves": 8,
            }
        }
        
        self.resources_by_tool[self.fallback] = {
            'default': {
                'minecraft:dark_oak_log': 1,
                'minecraft:dark_oak_sapling': 0.5,
                'minecraft:stick': 0.5,
                'minecraft:red_mushroom': 0.2,
                'minecraft:brown_mushroom': 0.2,
                'minecraft:apple': 0.2,
            },
            'minecraft:silk_touch': {
                'minecraft:dark_oak_leaves': 1,
                'minecraft:brown_mushroom_block': 0.2,
                'minecraft:red_mushroom_block': 0.2,
                'minecraft:mushroom_stem': 0.2,
            }
        }