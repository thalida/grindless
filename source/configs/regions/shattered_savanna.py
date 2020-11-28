from .savanna import Savanna

class ShatteredSavanna(Savanna):
    def __init__(self):
        super().__init__()
        self.name = 'shattered_savanna'
        self.display_name = 'Shattered Savanna'
        

        self.resources_by_tool['shovel'] = {
            'default': {
                "minecraft:dirt": 1,
                "minecraft:wheat_seeds": 0.5,
            },
            'minecraft:silk_touch': {
                "minecraft:grass_block": 1,
                "minecraft:coarse_dirt": 1,
                "minecraft:wheat_seeds": 0.5,
            }
        }

        self.resources_by_tool['pickaxe'] = {
            'default': {
                'minecraft:cobblestone': 1,
            },
            'minecraft:silk_touch': {
                'minecraft:stone': 1,
            }
        }