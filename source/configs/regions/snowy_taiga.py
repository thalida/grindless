from .taiga import Taiga

class SnowyTaiga(Taiga):
    def __init__(self):
        self.name = 'snowy_taiga'
        self.display_name = 'Snowy Taiga'

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

        self.resources_by_tool['hoe'] = {
            'default': {
                'items': {
                    "minecraft:wheat_seeds": 1,
                    "minecraft:sweet_berries": 0.5,
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
                    "minecraft:spruce_leaves": 8,
                    "minecraft:grass": 2,
                    "minecraft:fern": 1,
                    "minecraft:large_fern": 0.4,
                    "minecraft:sweet_berries": 0.5,
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
                    "minecraft:sweet_berries": 0.3,
                    "minecraft:snow_ball": 0.5,
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