from ..base_region import BaseRegion

class SnowyTundra(BaseRegion):
    def __init__(self):
        self.name = 'snowy_tundra'
        self.display_name = 'Snowy Tundra'

        self.items = {
            'minecraft:spruce_log': 2,
            'minecraft:spruce_leaves': 2,
            'minecraft:spruce_sapling': 1,
            'minecraft:ice': 2,
            'minecraft:snow': 2,
            'minecraft:snowball': 2,
            'minecraft:grass_block': 0.5,
            'minecraft:dirt': 1,
            'minecraft:grass': 2,
            'minecraft:wheat_seeds': 0.5,
        }