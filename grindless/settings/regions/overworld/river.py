from ..base_region import BaseRegion

class River(BaseRegion):
    def setup_region(self):
        self.name = 'river'
        self.display_name = 'River'

        self.items = {
                'minecraft:grass_block': 1,
                'minecraft:sand': 1,
                'minecraft:dirt': 1,
                'minecraft:sugar_cane': 0.25,
                'minecraft:clay': 0.25,
                'minecraft:clay_ball': 0.25,
                'minecraft:gravel': 0.25,
                'minecraft:flint': 0.25,
        }
