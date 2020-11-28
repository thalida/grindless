from .base_region import BaseRegion

class GravellyMountains(BaseRegion):
    def __init__(self):
        self.name = 'gravelly_mountains'
        self.display_name = 'Gravelly Mountains'

        self.resources_by_tool = {}
        self.resources_by_tool['shovel'] = {
            'default': {
                'minecraft:gravel': 2,
                'minecraft:flint': 1,
            },
            'minecraft:looting': {
                'minecraft:flint': 2,
                'minecraft:gravel': 1,
            },
            'minecraft:silk_touch': {
                'minecraft:gravel': 2,
            }
        }
        
        self.resources_by_tool['pickaxe'] = {
            'default': {
                'minecraft:cobblestone': 0.5,
            },
            'minecraft:silktouch': {
                'minecraft:stone': 0.5,
            }
        }
        
        self.resources_by_tool[self.fallback] = self.resources_by_tool['shovel']