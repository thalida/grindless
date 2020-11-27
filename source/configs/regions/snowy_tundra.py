from .base_region import BaseRegion

class SnowyTundra(BaseRegion):
    def __init__(self):
        self.name = 'snowy_tundra'
        self.display_name = 'Snowy Tundra'

        self.resources_by_tool = {}
        self.resources_by_tool['axe'] = {
            'default': {
                'items': {
                    'minecraft:spruce_log': 1.25,
                    'minecraft:spruce_sapling': 0.5,
                },
                'damage': 0.25
            },
            'minecraft:silk_touch': {
                'items': {
                    'minecraft:spruce_leaves': 1,
                },
            },
            'minecraft:unbreaking': {
                'damage': 0.125
            }
        }
        
        self.resources_by_tool['pickaxe'] = {
            'default': {
                'items': {},
                'damage': 0
            },
            'minecraft:silk_touch': {
                'items': {
                    'minecraft:ice': 1,
                }
            },
            'minecraft:unbreaking': {
                'damage': 0.125
            }
        }

        self.resources_by_tool['hoe'] = {
            'default': {
                'items': {
                    "minecraft:wheat_seeds": 0.5,
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
                    "minecraft:snowball": 1,
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
                    "minecraft:spruce_leaves": 8,
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
                    "minecraft:snowball": 0.5,
                },
                'damage': 0.25
            },
            'minecraft:silk_touch': {
                'items': {
                    'minecraft:spruce_leaves': 1,
                },
            },
            'minecraft:unbreaking': {
                'damage': 0.125
            }
        }