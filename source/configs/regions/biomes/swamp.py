from ..base_region import BaseRegion

class Swamp(BaseRegion):
    def __init__(self):
        self.name = 'swamp'
        self.display_name = 'Swamp'

        self.items = {
                'minecraft:oak_log': 1,
                'minecraft:oak_sapling': 0.5,
                'minecraft:apple': 0.2,
                'minecraft:oak_leaves': 1,
                'minecraft:brown_mushroom_block': 0.2,
                'minecraft:red_mushroom_block': 0.2,
                'minecraft:mushroom_stem': 0.2,
        }

        self.resources_by_tool = {}
        self.resources_by_tool['axe'] = {
            'default': {
                'minecraft:oak_log': 1,
                'minecraft:oak_sapling': 0.5,
                'minecraft:apple': 0.2,
            },
            'minecraft:silk_touch': {
                'minecraft:oak_leaves': 1,
                'minecraft:brown_mushroom_block': 0.2,
                'minecraft:red_mushroom_block': 0.2,
                'minecraft:mushroom_stem': 0.2,
            }
        }

        self.resources_by_tool['hoe'] = {
            'default': {
                'minecraft:red_mushroom': 0.2,
                'minecraft:brown_mushroom': 0.2,
                "minecraft:wheat_seeds": 0.5,
                "minecraft:lily_pad": 1,
                "minecraft:blue_orchid": 0.2,
            },
        }

        self.resources_by_tool['shovel'] = {
            'default': {
                "minecraft:dirt": 1,
                "minecraft:wheat_seeds": 0.25,
                'minecraft:clay_ball': 0.2,
            },
            'minecraft:silk_touch': {
                "minecraft:grass_block": 1,
                'minecraft:clay': 0.2,
                "minecraft:wheat_seeds": 0.25,
            }
        }

        self.resources_by_tool['shears'] = {
            'default': {
                "minecraft:oak_leaves": 8,
                "minecraft:vine": 6,
                "minecraft:dead_bush": 1,
                "minecraft:seagrass": 0.5,
            }
        }
        
        self.resources_by_tool[self.fallback] = {
            'default': {
                'minecraft:oak_log': 1,
                'minecraft:oak_sapling': 0.5,
                'minecraft:stick': 0.5,
                'minecraft:red_mushroom': 0.2,
                'minecraft:brown_mushroom': 0.2,
                'minecraft:apple': 0.2,
            },
            'minecraft:silk_touch': {
                'minecraft:oak_leaves': 1,
            }
        }