from .river import River

class FrozenRiver(River):
    def __init__(self):
        self.name = 'frozen_river'
        self.display_name = 'Frozen River'

        self.resources_by_tool = {}
        self.resources_by_tool['shovel'] = {
            'default': {
                'items': {
                    'minecraft:dirt': 0.5,
                    'minecraft:clay_ball': 0.25,
                    'minecraft:sand': 0.25,
                    'minecraft:gravel': 0.25,
                    'minecraft:flint': 0.125,
                },
                'damage': 0.25
            },
            'minecraft:looting': {
                'items': {
                    'minecraft:dirt': 0.5,
                    'minecraft:clay_ball': 0.25,
                    'minecraft:sand': 0.25,
                    'minecraft:flint': 0.25,
                    'minecraft:gravel': 0.125,
                }
            },
            'minecraft:silk_touch': {
                'items': {
                    'minecraft:grass_block': 0.5,
                    'minecraft:clay': 0.25,
                    'minecraft:sand': 0.25,
                    'minecraft:gravel': 0.25,
                }
            },
            'minecraft:unbreaking': {
                'damage': 0.125
            }
        }
        self.resources_by_tool['pickaxe'] = {
            'default': {
                'items': {},
                'damage': 0
            },
            'minecraft:silk_touch': {
                'items': {
                    'minecraft:ice': 1,
                }
            },
            'minecraft:unbreaking': {
                'damage': 0.125
            }
        }
        
        self.resources_by_tool[self.fallback] = self.resources_by_tool['shovel']