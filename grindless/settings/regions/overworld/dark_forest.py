from ..base_region import BaseRegion

class DarkForest(BaseRegion):
    def setup_region(self):
        self.name = 'dark_forest'
        self.display_name = 'Dark Forest'

        self.items = {
            'minecraft:dark_oak_log': 4,
            'minecraft:dark_oak_leaves': 2,
            'minecraft:dark_oak_sapling': 1.5,
            'minecraft:apple': 0.5,
            'minecraft:dirt': 1,
            'minecraft:grass_block': 1,
            'minecraft:stick': 0.5,
            'minecraft:brown_mushroom_block': 0.5,
            'minecraft:red_mushroom_block': 0.5,
            'minecraft:mushroom_stem': 0.2,
            'minecraft:red_mushroom': 0.2,
            'minecraft:brown_mushroom': 0.2,
            'minecraft:wheat_seeds': 0.5,
            'minecraft:dandelion': 0.3,
            'minecraft:poppy': 0.3,
            'minecraft:rose_bush': 0.2,
            'minecraft:lilac': 0.2,
            'minecraft:peony': 0.2,
            'minecraft:lily_of_the_valley': 0.2,
        }
