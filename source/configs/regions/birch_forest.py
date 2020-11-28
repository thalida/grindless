from .forest import Forest

class BirchForest(Forest):
    def __init__(self):
        self.name = 'birch_forest'
        self.display_name = 'Birch Forest'

        self.resources_by_tool = {}
        self.resources_by_tool['axe'] = {
            'default': {
                'minecraft:birch_log': 1,
                'minecraft:birch_sapling': 0.5,
                'minecraft:stick': 0.5,
            },
            'minecraft:silk_touch': {
                'minecraft:birch_leaves': 1,
            },
        }

        self.resources_by_tool['hoe'] = {
            'default': {
                "minecraft:wheat_seeds": 1,
                "minecraft:dandelion": 0.5,
                "minecraft:poppy": 0.5,
                "minecraft:rose_bush": 0.25,
                "minecraft:lilac": 0.25,
                "minecraft:peony": 0.25,
                "minecraft:lily_of_the_valley": 0.25,
            },
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
                "minecraft:birch_leaves": 8,
                "minecraft:grass": 2,
            }
        }
        
        self.resources_by_tool[self.fallback] = self.resources_by_tool['axe']