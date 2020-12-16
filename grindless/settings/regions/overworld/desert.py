from ..base_region import BaseRegion

class Desert(BaseRegion):
    def setup_region(self):
        self.name = 'desert'
        self.display_name = 'Desert'

        self.items = {
            'minecraft:sand': 4,
            'minecraft:sandstone': 2,
            'minecraft:stick': 1,
            'minecraft:dead_bush': 2,
            'minecraft:cactus': 0.25,
        }
