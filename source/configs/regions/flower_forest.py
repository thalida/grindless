from .forest import Forest

class FlowerForest(Forest):
    def __init__(self):
        self.name = 'flower_forest'
        self.display_name = 'Flower Forest'

        self.resources_by_tool = {}
        self.resources_by_tool['axe'] = {
            'default': {
                'minecraft:oak_log': 1,
                'minecraft:birch_log': 1,
                'minecraft:oak_sapling': 0.5,
                'minecraft:birch_sapling': 0.5,
                'minecraft:stick': 0.5,
                'minecraft:apple': 0.25,
            },
            'minecraft:silk_touch': {
                'minecraft:oak_leaves': 1,
                'minecraft:birch_leaves': 1,
            }
        }

        self.resources_by_tool['hoe'] = {
            'default': {
                "minecraft:wheat_seeds": 1,
                "minecraft:dandelion": 0.25,
                "minecraft:poppy": 0.25,
                "minecraft:allium": 0.25,
                "minecraft:azure_bluet": 0.25,
                "minecraft:oxeye_daisy": 0.25,
                "minecraft:cornflower": 0.25,
                "minecraft:rose_bush": 0.25,
                "minecraft:lilac": 0.25,
                "minecraft:peony": 0.25,
                "minecraft:lily_of_the_valley": 0.25,
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
                "minecraft:oak_leaves": 8,
                "minecraft:birch_leaves": 8,
                "minecraft:grass": 2,
            }
        }
        
        self.resources_by_tool[self.fallback] = self.resources_by_tool['axe']