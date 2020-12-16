from ..base_region import BaseRegion

class Jungle(BaseRegion):
    def setup_region(self):
        self.name = 'jungle'
        self.display_name = 'Jungle'

        self.items = {
            'minecraft:jungle_log': 2,
            'minecraft:jungle_leaves': 2,
            'minecraft:jungle_sapling': 1,
            'minecraft:cocoa_beans': 0.5,
            'minecraft:bamboo': 0.5,
            'minecraft:melon_slice': 0.5,
            'minecraft:melon': 0.5,
            'minecraft:dirt': 0.5,
            'minecraft:wheat_seeds': 0.25,
            'minecraft:vine': 2,
        }
