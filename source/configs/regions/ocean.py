from .base_region import BaseRegion

class Ocean(BaseRegion):
    def __init__(self):
        self.name = 'ocean'
        self.display_name = 'Ocean'

        self.resources_by_tool = {}
        self.resources_by_tool['shovel'] = {
            'default': {
                'items': {
                    'minecraft:sand': 1,
                    'minecraft:gravel': 0.5,
                    'minecraft:flint': 0.2,
                    'minecraft:dirt': 0.5,
                    'minecraft:clay_ball': 0.24,
                },
                'damage': 0.25
            },
            'minecraft:looting': {
                'items': {
                    'minecraft:sand': 1,
                    'minecraft:flint': 0.5,
                    'minecraft:gravel': 0.2,
                    'minecraft:dirt': 0.5,
                    'minecraft:clay_ball': 0.24,
                }
            },
            'minecraft:silk_touch': {
                'items': {
                    'minecraft:sand': 1,
                    'minecraft:gravel': 0.5,
                    'minecraft:dirt': 0.5,
                    'minecraft:clay': 0.24,
                }
            },
            'minecraft:unbreaking': {
                'damage': 0.125
            }
        }

        self.resources_by_tool['shears'] = {
            'default': {
                'items': {
                    "minecraft:kelp": 1,
                    "minecraft:seagrass": 1,
                },
                'damage': 1.5
            },
            'minecraft:unbreaking': {
                'damage': 0.75
            }
        }
        
        self.resources_by_tool[self.fallback] = self.resources_by_tool['shovel']