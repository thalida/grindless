from .badlands_plateau import BadlandsPlateau

class ModifiedBadlandsPlateau(BadlandsPlateau):
    def __init__(self):
        super().__init__()
        self.name = 'modified_badlands_plateau'
        self.display_name = 'Modified Badlands Plateau'

        self.resources_by_tool['axe'] = {
            'default': {
                'items': {
                    "minecraft:cactus": 0.25,
                    'minecraft:oak_log': 1,
                    'minecraft:oak_sapling': 0.5,
                    'minecraft:stick': 0.5,
                    'minecraft:apple': 0.25,
                },
                'damage': 0.25
            },
            'minecraft:silk_touch': {
                'items': {
                    'minecraft:oak_leaves': 1,
                },
            },
            'minecraft:unbreaking': {
                'damage': 0.125
            }
        }

        self.resources_by_tool['shears'] = {
            'default': {
                'items': {
                    "minecraft:dead_bush": 2,
                    "minecraft:oak_leaves": 1,
                },
                'damage': 1.5
            },
            'minecraft:unbreaking': {
                'damage': 0.75
            }
        }