from ..base_region import BaseRegion

class Mountains(BaseRegion):
    def __init__(self):
        self.name = 'mountains'
        self.display_name = 'Mountains'

        self.items = {
            'minecraft:oak_log': 1,
            'minecraft:spruce_log': 1,
            'minecraft:oak_leaves': 1,
            'minecraft:spruce_leaves': 1,
            'minecraft:spruce_sapling': 0.5,
            'minecraft:oak_sapling': 0.5,
            'minecraft:cobblestone': 4,
            'minecraft:stone': 4,
            'minecraft:wheat_seeds': 0.5,
            'minecraft:dirt': 1,
            'minecraft:snow': 1,
            'minecraft:snowball': 0.5,
            'minecraft:grass': 1,
        }