from ..base_region import BaseRegion

class Taiga(BaseRegion):
    def setup_region(self):
        self.name = 'taiga'
        self.display_name = 'Taiga'

        self.items = {
                'minecraft:spruce_log': 4,
                'minecraft:spruce_leaves': 2,
                'minecraft:spruce_sapling': 1,
                "minecraft:grass_block": 1,
                "minecraft:dirt": 1,
                "minecraft:wheat_seeds": 1,
                "minecraft:grass": 2,
                "minecraft:fern": 1,
                "minecraft:large_fern": 0.5,
                "minecraft:sweet_berries": 0.5,
        }
