from .forest import Forest

class BirchForest(Forest):
    def setup_region(self):
        self.name = 'birch_forest'
        self.display_name = 'Birch Forest'

        self.items = {
            'minecraft:birch_log': 4,
            'minecraft:birch_leaves': 2,
            'minecraft:birch_sapling': 1,
            'minecraft:stick': 0.5,

            'minecraft:grass_block': 1,
            'minecraft:dirt': 1,
            'minecraft:wheat_seeds': 1,

            'minecraft:dandelion': 0.5,
            'minecraft:poppy': 0.5,
            'minecraft:rose_bush': 0.25,
            'minecraft:lilac': 0.25,
            'minecraft:peony': 0.25,
            'minecraft:lily_of_the_valley': 0.25,
        }
