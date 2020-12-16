from .forest import Forest

class FlowerForest(Forest):
    def setup_region(self):
        self.name = 'flower_forest'
        self.display_name = 'Flower Forest'

        self.items = {
            'minecraft:oak_log': 2,
            'minecraft:birch_log': 2,
            'minecraft:oak_leaves': 2,
            'minecraft:birch_leaves': 1,
            'minecraft:oak_sapling': 0.5,
            'minecraft:birch_sapling': 0.5,
            'minecraft:stick': 0.5,
            'minecraft:apple': 0.25,
            'minecraft:grass_block': 1,
            'minecraft:dirt': 1,
            'minecraft:wheat_seeds': 1,
            'minecraft:grass': 1,
            'minecraft:dandelion': 0.5,
            'minecraft:poppy': 0.5,
            'minecraft:allium': 0.5,
            'minecraft:azure_bluet': 0.5,
            'minecraft:oxeye_daisy': 0.5,
            'minecraft:cornflower': 0.5,
            'minecraft:rose_bush': 0.5,
            'minecraft:lilac': 0.5,
            'minecraft:peony': 0.5,
            'minecraft:lily_of_the_valley': 0.5,
        }
