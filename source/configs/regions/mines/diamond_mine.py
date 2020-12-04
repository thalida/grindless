from ..base_region import BaseRegion

class DiamondMine(BaseRegion):
    def __init__(self):
        self.name = 'diamond_mine'
        self.display_name = 'Diamond Mine'
        self.region_type = 'mine'
        self.y_range = [0, 16]
        self.items = {
            'minecraft:coal': 2,
            'minecraft:coal_ore': 2,
            'minecraft:iron_ore': 1,
            'minecraft:gold_ore': 1,
            'minecraft:redstone': 0.5,
            'minecraft:redstone_ore': 1,
            'minecraft:lapis_lazuli': 0.5,
            'minecraft:lapis_ore': 1,
            'minecraft:emerald': 0.1,
            'minecraft:emerald_ore': 0.1,
            'minecraft:diamond': 0.25,
            'minecraft:diamond_ore': 0.5,
        }