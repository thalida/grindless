from ..base_region import BaseRegion

class CrimsonForest(BaseRegion):
    def setup_region(self):
        self.name = 'crimson_forest'
        self.display_name = 'Crimson Forest'
        self.region_type = 'nether'

        self.items = {
            'minecraft:crimson_nylium': 4,
            'minecraft:nether_wart_block': 4,
            'minecraft:crimson_stem': 4,
            'minecraft:crimson_roots': 2,
            'minecraft:crimson_fungus': 2,
            'minecraft:warped_fungus': 1,
            'minecraft:weeping_vines': 1,
            'minecraft:netherrack': 1,
            'minecraft:shroomlight': 1,
            'minecraft:nether_sprouts': 1,
            'minecraft:blackstone': 0.5,
        }
