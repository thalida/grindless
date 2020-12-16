from .taiga import Taiga

class GiantTreeTaiga(Taiga):
    def setup_region(self):
        self.name = 'giant_tree_taiga'
        self.display_name = 'Giant Tree Taiga'

        self.items = {
            'minecraft:spruce_log': 4,
            'minecraft:spruce_leaves': 1,
            'minecraft:spruce_sapling': 0.5,
            'minecraft:mossy_cobblestone': 0.5,
            'minecraft:dirt': 1,
            'minecraft:podzol': 1,
            'minecraft:grass_block': 0.5,
            'minecraft:coarse_dirt': 0.5,
            'minecraft:wheat_seeds': 1,
            'minecraft:sweet_berries': 0.5,
            'minecraft:red_mushroom': 0.2,
            'minecraft:brown_mushroom': 0.2,
            'minecraft:grass': 2,
            'minecraft:fern': 1,
            'minecraft:large_fern': 0.5,
            'minecraft:dead_bush': 0.5,
        }
