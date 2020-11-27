from .base_region import BaseRegion

class MushroomFields(BaseRegion):
    def __init__(self):
        self.name = 'mushroom_fields'
        self.display_name = 'Mushroom Fields'

        self.resources_by_tool = {}
        self.resources_by_tool['axe'] = {
            'default': {
                'items': {},
                'damage': 0.25
            },
            'minecraft:silk_touch': {
                'items': {
                    'minecraft:brown_mushroom_block': 0.2,
                    'minecraft:red_mushroom_block': 0.2,
                    'minecraft:mushroom_stem': 0.2,
                },
            },
            'minecraft:unbreaking': {
                'damage': 0.125
            }
        }

        self.resources_by_tool['hoe'] = {
            'default': {
                'items': {
                    'minecraft:red_mushroom': 0.2,
                    'minecraft:brown_mushroom': 0.2,
                },
                'damage': 0.25
            },
            'minecraft:unbreaking': {
                'damage': 0.125
            },
            'minecraft:silk_touch': {
                'items': {
                    'minecraft:brown_mushroom_block': 0.2,
                    'minecraft:red_mushroom_block': 0.2,
                    'minecraft:mushroom_stem': 0.2,
                }
            }
        }

        self.resources_by_tool['shovel'] = {
            'default': {
                'items': {
                    "minecraft:dirt": 1,
                },
                'damage': 0.25
            },
            'minecraft:silk_touch': {
                'items': {
                    "minecraft:mycelium": 1,
                },
            },
            'minecraft:unbreaking': {
                'damage': 0.125
            }
        }
        
        self.resources_by_tool[self.fallback] = {
            'default': {
                'items': {
                    'minecraft:dirt': 1,
                    'minecraft:red_mushroom': 0.2,
                    'minecraft:brown_mushroom': 0.2,
                },
                'damage': 0.25
            },
            'minecraft:silk_touch': {
                'items': {
                    'minecraft:mycelium': 1,
                    'minecraft:brown_mushroom_block': 0.2,
                    'minecraft:red_mushroom_block': 0.2,
                    'minecraft:mushroom_stem': 0.2,
                },
            },
            'minecraft:unbreaking': {
                'damage': 0.125
            }
        }