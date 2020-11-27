from .base_region import BaseRegion

class GravellyMountains(BaseRegion):
    def __init__(self):
        self.name = 'gravelly_mountains'
        self.display_name = 'Gravelly Mountains'

        self.resources_by_tool = {}
        self.resources_by_tool['shovel'] = {
            'default': {
                'items': {
                    'minecraft:gravel': 2,
                    'minecraft:fint': 1,
                },
                'damage': 0.25
            },
            'minecraft:looting': {
                'items': {
                    'minecraft:flint': 2,
                    'minecraft:gravel': 1,
                }
            },
            'minecraft:silk_touch': {
                'items': {
                    'minecraft:gravel': 2,
                }
            },
            'minecraft:unbreaking': {
                'damage': 0.125
            }
        }
        self.resources_by_tool['pickaxe'] = {
            'default': {
                'items': {
                    'minecraft:cobblestone': 0.5,
                },
                'damage': 0.25
            },
            'silktouch': {
                'items': {
                    'minecraft:stone': 0.5,
                },
                'damage': 0.25
            },
            'minecraft:unbreaking': {
                'damage': 0.125
            }
        }
        
        self.resources_by_tool[self.fallback] = self.resources_by_tool['shovel']