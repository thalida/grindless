from ..base_region import BaseRegion

class River(BaseRegion):
    def __init__(self):
        self.name = 'river'
        self.display_name = 'River'

        self.items = {
                'minecraft:dirt': 1,
                'minecraft:sugar_cane': 0.25,
                'minecraft:clay_ball': 0.25,
                'minecraft:sand': 0.25,
                'minecraft:gravel': 0.25,
                'minecraft:flint': 0.125,
        }

        self.resources_by_tool = {}
        self.resources_by_tool['shovel'] = {
            'default': {
                'minecraft:dirt': 1,
                'minecraft:sugar_cane': 0.25,
                'minecraft:clay_ball': 0.25,
                'minecraft:sand': 0.25,
                'minecraft:gravel': 0.25,
                'minecraft:flint': 0.125,
            },
            'minecraft:fortune': {
                'minecraft:dirt': 1,
                'minecraft:sugar_cane': 0.25,
                'minecraft:clay_ball': 0.25,
                'minecraft:sand': 0.25,
                'minecraft:flint': 0.25,
                'minecraft:gravel': 0.125,
            },
            'minecraft:silk_touch': {
                'minecraft:grass_block': 1,
                'minecraft:sugar_cane': 0.25,
                'minecraft:clay': 0.25,
                'minecraft:sand': 0.25,
                'minecraft:gravel': 0.25,
            }
        }
        
        self.resources_by_tool[self.fallback] = self.resources_by_tool['shovel']