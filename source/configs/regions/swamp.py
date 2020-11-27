from .base_region import BaseRegion

class Swamp(BaseRegion):
    def __init__(self):
        self.name = 'swamp'
        self.display_name = 'Swamp'

        self.resources_by_tool = {}
        self.resources_by_tool['axe'] = {
            'default': {
                'items': {
                    'minecraft:oak_log': 1,
                    'minecraft:oak_sapling': 0.5,
                    'minecraft:apple': 0.2,
                },
                'damage': 0.25
            },
            'minecraft:silk_touch': {
                'items': {
                    'minecraft:oak_leaves': 1,
                    'minecraft:brown_mushroom_block': 0.2,
                    'minecraft:red_mushroom_block': 0.2,
                    'minecraft:mushroom_stem': 0.2,
                },
            },
            'minecraft:unbreaking': {
                'damage': 0.125
            }
        }

        self.resources_by_tool['hoe'] = {
            'default': {
                'items': {
                    'minecraft:red_mushroom': 0.2,
                    'minecraft:brown_mushroom': 0.2,
                    "minecraft:wheat_seeds": 0.5,
                    "minecraft:lily_pad": 1,
                    "minecraft:blue_orchid": 0.2,
                },
                'damage': 0.25
            },
            'minecraft:unbreaking': {
                'damage': 0.125
            },
        }

        self.resources_by_tool['shovel'] = {
            'default': {
                'items': {
                    "minecraft:dirt": 1,
                    "minecraft:wheat_seeds": 0.25,
                    'minecraft:clay_ball': 0.2,
                },
                'damage': 0.25
            },
            'minecraft:silk_touch': {
                'items': {
                    "minecraft:grass_block": 1,
                    'minecraft:clay': 0.2,
                    "minecraft:wheat_seeds": 0.25,
                },
            },
            'minecraft:unbreaking': {
                'damage': 0.125
            }
        }

        self.resources_by_tool['shears'] = {
            'default': {
                'items': {
                    "minecraft:oak_leaves": 8,
                    "minecraft:vines": 6,
                    "minecraft:dead_bush": 1,
                    "minecraft:seagrass": 0.5,
                },
                'damage': 1.5
            },
            'minecraft:unbreaking': {
                'damage': 0.75
            }
        }
        
        self.resources_by_tool[self.fallback] = {
            'default': {
                'items': {
                    'minecraft:oak_log': 1,
                    'minecraft:oak_sapling': 0.5,
                    'minecraft:stick': 0.5,
                    'minecraft:red_mushroom': 0.2,
                    'minecraft:brown_mushroom': 0.2,
                    'minecraft:apple': 0.2,
                },
                'damage': 0.25
            },
            'minecraft:silk_touch': {
                'items': {
                    'minecraft:oak_leaves': 1,
                },
            },
            'minecraft:unbreaking': {
                'damage': 0.125
            }
        }