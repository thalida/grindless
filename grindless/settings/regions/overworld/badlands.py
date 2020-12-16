from ..base_region import BaseRegion

class Badlands(BaseRegion):
    def setup_region(self):
        self.name = 'badlands'
        self.display_name = 'Badlands'
        self.items = {
            'minecraft:terracotta': 1,
            'minecraft:red_terracotta': 0.5,
            'minecraft:orange_terracotta': 0.5,
            'minecraft:yellow_terracotta': 0.5,
            'minecraft:white_terracotta': 0.5,
            'minecraft:light_gray_terracotta': 0.5,
            'minecraft:brown_terracotta': 0.5,

            'minecraft:red_sand': 2,
            'minecraft:dead_bush': 1,
            'minecraft:stick': 0.25,

            'minecraft:cactus': 1,
        }
