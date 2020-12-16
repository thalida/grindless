from ..base_region import BaseRegion

class Forest(BaseRegion):
    def setup_region(self):
        self.name = 'forest'
        self.display_name = 'Forest'

        self.items = {
            'minecraft:oak_log': 2,
            'minecraft:birch_log': 2,
            'minecraft:oak_leaves': 2,
            'minecraft:birch_leaves': 2,
            'minecraft:oak_sapling': 0.5,
            'minecraft:birch_sapling': 0.5,
            'minecraft:stick': 0.5,
            'minecraft:apple': 0.25,
            'minecraft:grass_block': 1,
            'minecraft:dirt': 1,
            'minecraft:grass': 2,
            'minecraft:wheat_seeds': 1,
            'minecraft:dandelion': 0.5,
            'minecraft:poppy': 0.5,
            'minecraft:rose_bush': 0.25,
            'minecraft:lilac': 0.25,
            'minecraft:peony': 0.25,
            'minecraft:lily_of_the_valley': 0.25,
        }
