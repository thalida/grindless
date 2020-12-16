from ..base_region import BaseRegion

class WarpedForest(BaseRegion):
    def setup_region(self):
        self.name = 'warped_forest'
        self.display_name = 'Warped Forest'
        self.region_type = 'nether'

        self.items = {
            'minecraft:warped_nylium': 4,
            'minecraft:warped_wart_block': 4,
            'minecraft:warped_stem': 4,
            'minecraft:warped_roots': 2,
            'minecraft:warped_fungus': 2,
            'minecraft:crimson_fungus': 1,
            'minecraft:twisting_vines': 1,
            'minecraft:netherrack': 1,
            'minecraft:shroomlight': 1,
            'minecraft:nether_sprouts': 1,
            'minecraft:soul_sand': 0.5,
            'minecraft:blackstone': 0.5,
        }
