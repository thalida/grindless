from .base_region import BaseRegion

class Ocean(BaseRegion):
    def __init__(self):
        self.name = 'ocean'
        self.display_name = 'Ocean'

        self.resources_by_tool = {}
        self.resources_by_tool['shovel'] = {
            'default': {
                'minecraft:sand': 1,
                'minecraft:gravel': 0.5,
                'minecraft:flint': 0.2,
                'minecraft:dirt': 0.5,
                'minecraft:clay_ball': 0.24,
            },
            'minecraft:fortune': {
                'minecraft:sand': 1,
                'minecraft:flint': 0.5,
                'minecraft:gravel': 0.2,
                'minecraft:dirt': 0.5,
                'minecraft:clay_ball': 0.24,
            },
            'minecraft:silk_touch': {
                'minecraft:sand': 1,
                'minecraft:gravel': 0.5,
                'minecraft:dirt': 0.5,
                'minecraft:clay': 0.24,
            }
        }

        self.resources_by_tool['shears'] = {
            'default': {
                "minecraft:kelp": 1,
                "minecraft:seagrass": 1,
            }
        }
        
        self.resources_by_tool[self.fallback] = self.resources_by_tool['shovel']