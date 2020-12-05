from .badlands_plateau import BadlandsPlateau

class ModifiedBadlandsPlateau(BadlandsPlateau):
    def __init__(self):
        super().__init__()
        self.name = 'modified_badlands_plateau'
        self.display_name = 'Modified Badlands Plateau'

        self.items = {
            'minecraft:cactus': 1,
            'minecraft:oak_log': 1,
            'minecraft:oak_leaves': 1,
            'minecraft:oak_sapling': 1,
            'minecraft:stick': 0.5,
            'minecraft:apple': 0.25,
            'minecraft:dead_bush': 2,
        }