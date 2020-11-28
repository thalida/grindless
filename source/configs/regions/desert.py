from .base_region import BaseRegion

class Desert(BaseRegion):
    def __init__(self):
        self.name = 'desert'
        self.display_name = 'Desert'

        self.resources_by_tool = {}
        self.resources_by_tool['pickaxe'] = {
            'default': {
                'minecraft:sandstone': 0.5,
                'minecraft:stick': 0.25,
            }
        }

        self.resources_by_tool['hoe'] = {
            'default': {
                "minecraft:stick": 1,
            }
        }

        self.resources_by_tool['shovel'] = {
            'default': {
                "minecraft:sand": 1,
                "minecraft:stick": 0.25,
            }
        }

        self.resources_by_tool['axe'] = {
            'default': {
                "minecraft:cactus": 0.25,
            }
        }

        self.resources_by_tool['shears'] = {
            'default': {
                "minecraft:dead_bush": 2,
            }
        }
        
        self.resources_by_tool[self.fallback] = self.resources_by_tool['shovel']