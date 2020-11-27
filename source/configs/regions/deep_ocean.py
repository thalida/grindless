from .ocean import Ocean

class DeepOcean(Ocean):
    def __init__(self):
        self.name = 'deep_ocean'
        self.display_name = 'Deep Ocean'

        self.resources_by_tool = {}
        self.resources_by_tool['shovel'] = {
            'default': {
                'items': {
                    'minecraft:sand': 1,
                    'minecraft:gravel': 0.5,
                    'minecraft:fint': 0.2,
                    "minecraft:kelp": 1,
                },
                'damage': 0.25
            },
            'minecraft:looting': {
                'items': {
                    'minecraft:sand': 1,
                    'minecraft:flint': 0.5,
                    'minecraft:gravel': 0.2,
                }
            },
            'minecraft:silk_touch': {
                'items': {
                    'minecraft:sand': 1,
                    'minecraft:gravel': 0.5,
                }
            },
            'minecraft:unbreaking': {
                'damage': 0.125
            }
        }
        self.resources_by_tool['pickaxe'] = {
            'default': {
                'items': {
                    'minecraft:magma_block': 0.2,
                },
                'damage': 0.25
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