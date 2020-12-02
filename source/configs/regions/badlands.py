from .base_region import BaseRegion

class Badlands(BaseRegion):
    def __init__(self):
        self.name = 'badlands'
        self.display_name = 'Badlands'
        self.items = {
            'minecraft:terracotta': 2,
            'minecraft:red_sand': 2,
            'minecraft:cactus': 1,
            'minecraft:dead_bush': 1,
            'minecraft:stick': 0.5,
        }

        self.resources_by_tool = {}
        self.resources_by_tool['pickaxe'] = {
            'default': {
                'minecraft:terracotta': 1,
                'minecraft:red_terracotta': 0.5,
                'minecraft:orange_terracotta': 0.5,
                'minecraft:yellow_terracotta': 0.5,
                'minecraft:white_terracotta': 0.5,
                'minecraft:light_gray_terracotta': 0.5,
                'minecraft:brown_terracotta': 0.5,
                'minecraft:stick': 0.25,
            },
        }

        self.resources_by_tool['hoe'] = {
            'default': {
                "minecraft:stick": 1,
            },
        }

        self.resources_by_tool['shovel'] = {
            'default': {
                "minecraft:red_sand": 1,
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
        
        self.resources_by_tool[self.fallback] = self.resources_by_tool['pickaxe']