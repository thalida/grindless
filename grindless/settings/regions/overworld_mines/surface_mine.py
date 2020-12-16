from ..base_region import BaseRegion

class SurfaceMine(BaseRegion):
    def setup_region(self):
        self.name = 'surface_mine'
        self.display_name = 'Surface Mine'
        self.region_type = 'overworld_mine'
        self.y_range = [17, 55]
        self.items = {
            'minecraft:coal': 2,
            'minecraft:coal_ore': 2,
            'minecraft:iron_ore': 1,
        }
