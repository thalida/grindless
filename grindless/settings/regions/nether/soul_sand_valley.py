from ..base_region import BaseRegion

class SoulSandValley(BaseRegion):
    def setup_region(self):
        self.name = 'soul_sand_valley'
        self.display_name = 'Soul Sand Valley'
        self.region_type = 'nether'

        self.items = {
            'minecraft:soul_sand': 4,
            'minecraft:soul_soil': 4,
            'minecraft:netherrack': 2,
            'minecraft:basalt': 1,
            'minecraft:blackstone': 1,
            'minecraft:glowstone': 1,
            'minecraft:glowstone_dust': 0.5,
            'minecraft:crimson_roots': 0.5,
        }
