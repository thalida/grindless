from .ocean import Ocean

class DeepOcean(Ocean):
    def __init__(self):
        self.name = 'deep_ocean'
        self.display_name = 'Deep Ocean'

        self.resources_by_tool = {}
        self.resources_by_tool['shovel'] = {
            'default': {
                'minecraft:sand': 1,
                'minecraft:gravel': 0.5,
                'minecraft:flint': 0.2,
                "minecraft:kelp": 1,
            },
            'minecraft:looting': {
                'minecraft:sand': 1,
                'minecraft:flint': 0.5,
                'minecraft:gravel': 0.2,
            },
            'minecraft:silk_touch': {
                'minecraft:sand': 1,
                'minecraft:gravel': 0.5,
            },
        }
        self.resources_by_tool['pickaxe'] = {
            'default': {
                'minecraft:magma_block': 0.2,
            },
        }

        self.resources_by_tool['shears'] = {
            'default': {
                "minecraft:kelp": 1,
                "minecraft:seagrass": 1,
            }
        }
        
        self.resources_by_tool[self.fallback] = self.resources_by_tool['shovel']