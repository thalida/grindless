from .badlands_plateau import BadlandsPlateau

class ModifiedBadlandsPlateau(BadlandsPlateau):
    def __init__(self):
        super().__init__()
        self.name = 'modified_badlands_plateau'
        self.display_name = 'Modified Badlands Plateau'

        self.resources_by_tool['axe'] = {
            'default': {
                "minecraft:cactus": 0.25,
                'minecraft:oak_log': 1,
                'minecraft:oak_sapling': 0.5,
                'minecraft:stick': 0.5,
                'minecraft:apple': 0.25,
            },
            'minecraft:silk_touch': {
                'minecraft:oak_leaves': 1,
            }
        }

        self.resources_by_tool['shears'] = {
            'default': {
                "minecraft:dead_bush": 2,
                "minecraft:oak_leaves": 1,
            }
        }