from .base_region import BaseRegion

class TheEnd(BaseRegion):
    def __init__(self):
        self.name = 'the_end'
        self.display_name = 'The End'

        self.resources_by_tool = {}
        self.resources_by_tool['pickaxe'] = {
            'default': {
                'items': {
                    'minecraft:end_stone': 1,
                    'minecraft:obsidian': 0.2,
                },
                'damage': 0.25
            },
            'minecraft:unbreaking': {
                'damage': 0.125
            }
        }
        
        self.resources_by_tool['sword'] = {
            'default': {
                'items': {
                    'minecraft:shulker_box': 1,
                },
                'damage': 0.25
            },
            'minecraft:unbreaking': {
                'damage': 0.125
            }
        }
        
        
        self.resources_by_tool['axe'] = {
            'default': {
                'items': {
                    'minecraft:chorus_fruit': 1,
                    'minecraft:chorus_flower': 0.2,
                },
                'damage': 0.25
            },
            'minecraft:unbreaking': {
                'damage': 0.125
            }
        }
        
        self.resources_by_tool[self.fallback] = {
            'default': {
                'items': {
                    'minecraft:end_stone': 0.5,
                },
                'damage': 0.25
            },
            'minecraft:unbreaking': {
                'damage': 0.125
            }
        }
