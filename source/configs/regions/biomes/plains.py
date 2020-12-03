from ..base_region import BaseRegion

class Plains(BaseRegion):
    def __init__(self):
        self.name = 'plains'
        self.display_name = 'Plains'

        self.items = {
            'minecraft:oak_log': 1,
            'minecraft:oak_leaves': 1,
            'minecraft:oak_sapling': 0.5,
            'minecraft:stick': 0.5,
            'minecraft:apple': 0.25,
            "minecraft:grass_block": 4,
            "minecraft:dirt": 3,
            "minecraft:grass": 4,
            "minecraft:wheat_seeds": 2,
            "minecraft:azure_bluet": 0.5,
            "minecraft:oxeye_daisy": 0.5,
            "minecraft:cornflower": 0.5,
        }