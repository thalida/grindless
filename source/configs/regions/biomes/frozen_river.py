from .river import River

class FrozenRiver(River):
    def __init__(self):
        self.name = 'frozen_river'
        self.display_name = 'Frozen River'

        self.items = {
            'minecraft:ice': 1,
            'minecraft:grass_block': 0.5,
            'minecraft:dirt': 0.5,
            'minecraft:clay_ball': 0.25,
            'minecraft:sand': 0.25,
            'minecraft:gravel': 0.25,
            'minecraft:flint': 0.25,
        }