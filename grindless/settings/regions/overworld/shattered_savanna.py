from .savanna import Savanna

class ShatteredSavanna(Savanna):
    def setup_region(self):
        super().setup_region()
        self.name = 'shattered_savanna'
        self.display_name = 'Shattered Savanna'

        self.items = {
            'minecraft:grass_block': 1,
            'minecraft:coarse_dirt': 1,
            'minecraft:dirt': 1,
            'minecraft:wheat_seeds': 0.5,
            'minecraft:stone': 1,
            'minecraft:cobblestone': 1,
        }
