from ..base_region import BaseRegion

class Savanna(BaseRegion):
    def __init__(self):
        self.name = 'savanna'
        self.display_name = 'Savanna'

        self.items = {
            'minecraft:acacia_log': 2,
            'minecraft:oak_log': 0.5,
            'minecraft:acacia_leaves': 2,
            'minecraft:oak_leaves': 0.5,
            'minecraft:acacia_sapling': 1,
            'minecraft:oak_sapling': 0.25,
            'minecraft:stick': 0.5,
            'minecraft:grass_block': 2,
            'minecraft:grass': 2,
            'minecraft:dirt': 1,
            'minecraft:wheat_seeds': 1,
        }