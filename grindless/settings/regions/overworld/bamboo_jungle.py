from ..base_region import BaseRegion

class BambooJungle(BaseRegion):
    def setup_region(self):
        self.name = 'bamboo_jungle'
        self.display_name = 'Bamboo Jungle'
        self.items = {
            'minecraft:bamboo': 4,
            'minecraft:jungle_log': 2,
            'minecraft:jungle_leaves': 2,
            'minecraft:jungle_sapling': 1,

            'minecraft:cocoa_beans': 1,
            'minecraft:melon': 1,
            'minecraft:melon_slice': 1,

            'minecraft:grass_block': 0.5,
            'minecraft:dirt': 0.25,
            'minecraft:wheat_seeds': 0.5,
            'minecraft:podzol': 0.5,
            'minecraft:vine': 0.5,
        }
