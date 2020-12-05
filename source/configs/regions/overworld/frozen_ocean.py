from .ocean import Ocean

class FrozenOcean(Ocean):
    def __init__(self):
        self.name = 'frozen_ocean'
        self.display_name = 'Frozen Ocean'

        self.items = {
            'minecraft:snowball': 1,
            'minecraft:sand': 0.5,
            'minecraft:gravel': 0.5,
            'minecraft:flint': 0.5,
            'minecraft:clay_ball': 0.2,
            'minecraft:dirt': 0.1,
            'minecraft:ice': 1,
            'minecraft:packed_ice': 1,
            'minecraft:blue_ice': 0.5,
        }