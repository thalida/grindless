from ..base_region import BaseRegion

class MushroomFields(BaseRegion):
    def __init__(self):
        self.name = 'mushroom_fields'
        self.display_name = 'Mushroom Fields'

        self.items = {
                'minecraft:brown_mushroom_block': 0.2,
                'minecraft:red_mushroom_block': 0.2,
                'minecraft:mushroom_stem': 0.2,
        }

        self.resources_by_tool = {}
        self.resources_by_tool['axe'] = {
            'minecraft:silk_touch': {
                'minecraft:brown_mushroom_block': 0.2,
                'minecraft:red_mushroom_block': 0.2,
                'minecraft:mushroom_stem': 0.2,
            }
        }

        self.resources_by_tool['hoe'] = {
            'default': {
                'minecraft:red_mushroom': 0.2,
                'minecraft:brown_mushroom': 0.2,
            },
            'minecraft:silk_touch': {
                'minecraft:brown_mushroom_block': 0.2,
                'minecraft:red_mushroom_block': 0.2,
                'minecraft:mushroom_stem': 0.2,
            }
        }

        self.resources_by_tool['shovel'] = {
            'default': {
                "minecraft:dirt": 1,
            },
            'minecraft:silk_touch': {
                "minecraft:mycelium": 1,
            }
        }
        
        self.resources_by_tool[self.fallback] = {
            'default': {
                'minecraft:dirt': 1,
                'minecraft:red_mushroom': 0.2,
                'minecraft:brown_mushroom': 0.2,
            },
            'minecraft:silk_touch': {
                'minecraft:mycelium': 1,
                'minecraft:brown_mushroom_block': 0.2,
                'minecraft:red_mushroom_block': 0.2,
                'minecraft:mushroom_stem': 0.2,
            }
        }