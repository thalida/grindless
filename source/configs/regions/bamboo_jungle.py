from .base_region import BaseRegion

class Jungle(BaseRegion):
    def __init__(self):
        self.name = 'jungle'
        self.display_name = 'Jungle'

        self.resources_by_tool = {}
        self.resources_by_tool['axe'] = {
            'default': {
                'items': {
                    'minecraft:bamboo': 2,
                    'minecraft:jungle_log': 1,
                    'minecraft:jungle_sapling': 1,
                    'minecraft:cocoa_beans': 0.4,
                    'minecraft:oak_log': 0.25,
                    'minecraft:oak_sapling': 0.125,
                    'minecraft:melon_slice': 0.25,
                },
                'damage': 0.25
            },
            'minecraft:silk_touch': {
                'items': {
                    'minecraft:jungle_leaves': 2,
                    'minecraft:oak_leaves': 0.4,
                    'minecraft:melon': 0.25,
                },
            },
            'minecraft:unbreaking': {
                'damage': 0.125
            }
        }

        self.resources_by_tool['sword'] = {
            'default': {
                'items': {
                    "minecraft:bamboo": 2,
                },
                'damage': 0.25
            },
            'minecraft:unbreaking': {
                'damage': 0.125
            }
        }

        self.resources_by_tool['shovel'] = {
            'default': {
                'items': {
                    "minecraft:dirt": 1,
                    "minecraft:wheat_seeds": 0.25,
                },
                'damage': 0.25
            },
            'minecraft:silk_touch': {
                'items': {
                    "minecraft:grass_block": 1,
                    "minecraft:podzol_block": 0.8,
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
                    "minecraft:vines": 2,
                    "minecraft:jungle_leaves": 2,
                },
                'damage': 1.5
            },
            'minecraft:unbreaking': {
                'damage': 0.75
            }
        }
        
        self.resources_by_tool[self.fallback] = self.resources_by_tool['axe']