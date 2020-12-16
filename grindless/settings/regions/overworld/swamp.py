from ..base_region import BaseRegion

class Swamp(BaseRegion):
    def setup_region(self):
        self.name = 'swamp'
        self.display_name = 'Swamp'

        self.items = {
                'minecraft:oak_log': 2,
                'minecraft:oak_leaves': 2,
                'minecraft:oak_sapling': 1,
                'minecraft:apple': 0.2,
                'minecraft:grass_block': 1,
                'minecraft:dirt': 1,
                'minecraft:clay': 0.2,
                'minecraft:clay_ball': 0.2,
                'minecraft:brown_mushroom_block': 0.2,
                'minecraft:red_mushroom_block': 0.2,
                'minecraft:mushroom_stem': 0.2,
                'minecraft:red_mushroom': 0.2,
                'minecraft:brown_mushroom': 0.2,
                'minecraft:dead_bush': 1,
                'minecraft:stick': 0.5,
                'minecraft:wheat_seeds': 0.5,
                'minecraft:vine': 4,
                'minecraft:lily_pad': 4,
                'minecraft:blue_orchid': 0.2,
                'minecraft:seagrass': 0.5,
        }
