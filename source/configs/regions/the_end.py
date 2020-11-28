from .base_region import BaseRegion

class TheEnd(BaseRegion):
    def __init__(self):
        self.name = 'the_end'
        self.display_name = 'The End'

        self.resources_by_tool = {}
        self.resources_by_tool['pickaxe'] = {
            'default': {
                'minecraft:end_stone': 1,
                'minecraft:obsidian': 0.2,
            }
        }
        
        self.resources_by_tool['sword'] = {
            'default': {
                'minecraft:shulker_box': 1,
            }
        }
        
        
        self.resources_by_tool['axe'] = {
            'default': {
                'minecraft:chorus_fruit': 1,
                'minecraft:chorus_flower': 0.2,
            }
        }
        
        self.resources_by_tool[self.fallback] = {
            'default': {
                'minecraft:end_stone': 0.5,
            }
        }
