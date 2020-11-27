from .base_region import BaseRegion

class Badlands(BaseRegion):
    def __init__(self):
        self.name = 'badlands'
        self.display_name = 'Badlands'

        self.resources_by_tool = {}
        self.resources_by_tool['pickaxe'] = {
            'default': {
                'items': {
                    'minecraft:terracotta': 1,
                    'minecraft:red_terracotta': 0.5,
                    'minecraft:orange_terracotta': 0.5,
                    'minecraft:yellow_terracotta': 0.5,
                    'minecraft:white_terracotta': 0.5,
                    'minecraft:light_gray_terracotta': 0.5,
                    'minecraft:brown_terracotta': 0.5,
                    'minecraft:stick': 0.25,
                },
                'damage': 0.25
            },
            'minecraft:unbreaking': {
                'damage': 0.125
            }
        }

        self.resources_by_tool['hoe'] = {
            'default': {
                'items': {
                    "minecraft:stick": 1,
                },
                'damage': 0.25
            },
            'minecraft:unbreaking': {
                'damage': 0.125
            }
        }

        self.resources_by_tool['shovel'] = {
            'default': {
                'items': {
                    "minecraft:red_sand": 1,
                    "minecraft:stick": 0.25,
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
                    "minecraft:cactus": 0.25,
                },
                'damage': 0.15
            },
            'minecraft:unbreaking': {
                'damage': 0.15 / 2
            }
        }

        self.resources_by_tool['shears'] = {
            'default': {
                'items': {
                    "minecraft:dead_bush": 2,
                },
                'damage': 1.5
            },
            'minecraft:unbreaking': {
                'damage': 0.75
            }
        }
        
        self.resources_by_tool[self.fallback] = self.resources_by_tool['pickaxe']