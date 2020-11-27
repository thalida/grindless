from .base_region import BaseRegion

class Mountains(BaseRegion):
    def __init__(self):
        self.name = 'mountains'
        self.display_name = 'Mountains'

        self.resources_by_tool = {}
        self.resources_by_tool['axe'] = {
            'default': {
                'items': {
                    'minecraft:oak_log': 1,
                    'minecraft:oak_sapling': 0.5,
                    'minecraft:spruce_log': 1,
                    'minecraft:spruce_sapling': 0.5,
                },
                'damage': 0.25
            },
            'minecraft:silk_touch': {
                'items': {
                    'minecraft:spruce_leaves': 1,
                    'minecraft:oak_leaves': 1,
                },
            },
            'minecraft:unbreaking': {
                'damage': 0.125
            }
        }

        self.resources_by_tool['pickaxe'] = {
            'default': {
                'items': {
                    "minecraft:cobblestone": 1,
                },
                'damage': 0.25
            },
            'minecraft:silk_touch': {
                'items': {
                    "minecraft:stone": 1,
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
                    "minecraft:snow_ball": 0.5,
                    "minecraft:wheat_seeds": 0.2,
                },
                'damage': 0.25
            },
            'minecraft:silk_touch': {
                'items': {
                    "minecraft:snow": 1,
                    "minecraft:grass_block": 0.5,
                    "minecraft:wheat_seeds": 0.2,
                },
            },
            'minecraft:unbreaking': {
                'damage': 0.125
            }
        }

        self.resources_by_tool['shears'] = {
            'default': {
                'items': {
                    "minecraft:spruce_leaves": 4,
                    "minecraft:oak_leaves": 4,
                    "minecraft:grass": 2,
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
                    'minecraft:spruce_log': 1,
                    'minecraft:spruce_sapling': 0.3,
                    'minecraft:oak_log': 1,
                    'minecraft:oak_sapling': 0.3,
                    "minecraft:snow_ball": 0.5,
                },
                'damage': 0.25
            },
            'minecraft:silk_touch': {
                'items': {
                    'minecraft:spruce_leaves': 1,
                    'minecraft:oak_leaves': 1,
                },
            },
            'minecraft:unbreaking': {
                'damage': 0.125
            }
        }