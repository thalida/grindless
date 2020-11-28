from .taiga import Taiga

class SnowyTaiga(Taiga):
    def __init__(self):
        self.name = 'snowy_taiga'
        self.display_name = 'Snowy Taiga'

        self.resources_by_tool = {}
        self.resources_by_tool['axe'] = {
            'default': {
                'minecraft:spruce_log': 1.25,
                'minecraft:spruce_sapling': 0.5,
            },
            'minecraft:silk_touch': {
                'minecraft:spruce_leaves': 1,
            }
        }

        self.resources_by_tool['hoe'] = {
            'default': {
                "minecraft:wheat_seeds": 1,
                "minecraft:sweet_berries": 0.5,
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
                "minecraft:spruce_leaves": 8,
                "minecraft:grass": 2,
                "minecraft:fern": 1,
                "minecraft:large_fern": 0.4,
                "minecraft:sweet_berries": 0.5,
            }
        }
        
        self.resources_by_tool[self.fallback] = {
            'default': {
                'minecraft:spruce_log': 1,
                'minecraft:spruce_sapling': 0.3,
                "minecraft:sweet_berries": 0.3,
                "minecraft:snowball": 0.5,
            },
            'minecraft:silk_touch': {
                'minecraft:spruce_leaves': 1,
            }
        }