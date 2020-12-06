from .taiga import Taiga

class SnowyTaiga(Taiga):
    def __init__(self):
        self.name = 'snowy_taiga'
        self.display_name = 'Snowy Taiga'

        self.items = {
            'minecraft:spruce_log': 2,
            'minecraft:spruce_leaves': 2,
            'minecraft:spruce_sapling': 1,
            'minecraft:snow': 2,
            'minecraft:snowball': 2,
            'minecraft:grass_block': 0.5,
            'minecraft:dirt': 1,
            'minecraft:grass': 1,
            'minecraft:wheat_seeds': 0.5,
            'minecraft:sweet_berries': 0.5,
            'minecraft:fern': 1,
            'minecraft:large_fern': 0.4,
        }