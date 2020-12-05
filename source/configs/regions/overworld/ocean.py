from ..base_region import BaseRegion

class Ocean(BaseRegion):
    def __init__(self):
        self.name = 'ocean'
        self.display_name = 'Ocean'

        self.items = {
            'minecraft:sand': 2,
            'minecraft:gravel': 1,
            'minecraft:flint': 1,
            'minecraft:dirt': 1,
            'minecraft:clay_ball': 0.5,
            'minecraft:clay': 0.5,
            'minecraft:kelp': 3,
            'minecraft:seagrass': 3,
        }