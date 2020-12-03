from .taiga import Taiga

class GiantTreeTaiga(Taiga):
    def __init__(self):
        self.name = 'giant_tree_taiga'
        self.display_name = 'Giant Tree Taiga'

        self.items = {
                    'minecraft:spruce_log': 1.25,
                    'minecraft:spruce_sapling': 0.5,
                'minecraft:spruce_leaves': 1,
        }

        self.resources_by_tool = {}
        self.resources_by_tool['axe'] = {
            'default': {
                    'minecraft:spruce_log': 1.25,
                    'minecraft:spruce_sapling': 0.5,
            },
            'minecraft:silk_touch': {
                'minecraft:spruce_leaves': 1,
            },
        }

        self.resources_by_tool['pickaxe'] = {
            'default': {
                'minecraft:mossy_cobblestone': 0.5,
            },
        }

        self.resources_by_tool['hoe'] = {
            'default': {
                "minecraft:wheat_seeds": 1,
                "minecraft:sweet_berries": 0.5,
                'minecraft:red_mushroom': 0.2,
                'minecraft:brown_mushroom': 0.2,
            },
        }

        self.resources_by_tool['shovel'] = {
            'default': {
                "minecraft:dirt": 1,
                "minecraft:coarse_dirt": 0.5,
                "minecraft:wheat_seeds": 0.25,
            },
            'minecraft:silk_touch': {
                "minecraft:podzol": 1,
                "minecraft:grass_block": 0.5,
                "minecraft:coarse_dirt": 0.5,
                "minecraft:dirt": 0.25,
                "minecraft:wheat_seeds": 0.25,
            }
        }

        self.resources_by_tool['shears'] = {
            'default': {
                "minecraft:spruce_leaves": 8,
                "minecraft:grass": 2,
                "minecraft:fern": 1,
                "minecraft:large_fern": 0.5,
                "minecraft:dead_bush": 0.5,
            }
        }
        
        self.resources_by_tool[self.fallback] = {
            'default': {
                'minecraft:spruce_log': 1,
                'minecraft:spruce_sapling': 0.3,
                "minecraft:sweet_berries": 0.3,
                'minecraft:red_mushroom': 0.2,
                'minecraft:brown_mushroom': 0.2,
            },
            'minecraft:silk_touch': {
                'minecraft:spruce_leaves': 1,
            }
        }