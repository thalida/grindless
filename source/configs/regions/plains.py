from .base_region import BaseRegion

class Plains(BaseRegion):
    def __init__(self):
        self.name = 'plains'
        self.display_name = 'Plains'

        self.resources_by_tool = {}
        self.resources_by_tool['axe'] = {
            'default': {
                'items': {
                    'minecraft:oak_log': 1,
                    'minecraft:oak_sapling': 0.5,
                    'minecraft:stick': 0.5,
                    'minecraft:apple': 0.25,
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

        self.resources_by_tool['hoe'] = {
            'default': {
                'items': {
                    "minecraft:wheat_seeds": 1,
                    "minecraft:azure_bluet": 0.25,
                    "minecraft:oxeye_daisy": 0.25,
                    "minecraft:cornflower": 0.25,
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
                    "minecraft:oak_leaves": 4,
                    "minecraft:grass": 4,
                },
                'damage': 1.5
            },
            'minecraft:unbreaking': {
                'damage': 0.75
            }
        }
        
        self.resources_by_tool[self.fallback] = self.resources_by_tool['axe']