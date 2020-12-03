from ..base_region import BaseRegion

class BasaltDeltas(BaseRegion):
    def __init__(self):
        self.name = 'basalt_deltas'
        self.display_name = 'Basalt Deltas'
        self.items = {
            'minecraft:basalt': 4,
            'minecraft:blackstone': 2,
            'minecraft:netherrack': 1,
            'minecraft:magma_block': 1,
        }