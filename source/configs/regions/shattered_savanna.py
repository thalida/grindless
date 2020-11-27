from .savanna import Savanna

class ShatteredSavanna(Savanna):
    def __init__(self):
        super().__init__()
        self.name = 'shattered_savanna'
        self.display_name = 'Shattered Savanna'
        

        self.resources_by_tool['shovel'] = {
            'default': {
                'items': {
                    "minecraft:dirt": 1,
                    "minecraft:wheat_seeds": 0.5,
                },
                'damage': 0.25
            },
            'minecraft:silk_touch': {
                'items': {
                    "minecraft:grass_block": 1,
                    "minecraft:coarse_dirt": 1,
                    "minecraft:wheat_seeds": 0.5,
                },
            },
            'minecraft:unbreaking': {
                'damage': 0.125
            }
        }

        self.resources_by_tool['pickaxe'] = {
            'default': {
                'items': {
                    'minecraft:cobblestone': 1,
                },
                'damage': 0.25
            },
            'minecraft:silk_touch': {
                'items': {
                    'minecraft:stone': 1,
                },
            },
            'minecraft:unbreaking': {
                'damage': 0.125
            }
        }