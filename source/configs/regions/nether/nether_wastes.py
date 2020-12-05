from ..base_region import BaseRegion

class NetherWastes(BaseRegion):
    def __init__(self):
        self.name = 'nether_wastes'
        self.display_name = 'Nether Wastes'
        self.region_type = 'nether'

        self.items = {
            'minecraft:netherrack': 2,
            'minecraft:quartz': 1,
            'minecraft:gold_nugget': 1,
            'minecraft:magma_block': 0.5,
            'minecraft:blackstone': 0.5,
            'minecraft:glowstone_dust': 0.5,
            'minecraft:glowstone': 1,
            'minecraft:nether_quartz_ore': 1,
            'minecraft:nether_gold_ore': 1,
            'minecraft:soul_sand': 1,
            'minecraft:ancient_debris': 0.2,
        }