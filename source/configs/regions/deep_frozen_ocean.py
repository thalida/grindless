from .ocean import Ocean

class DeepFrozenOcean(Ocean):
    def __init__(self):
        self.name = 'deep_frozen_ocean'
        self.display_name = 'Deep Frozen Ocean'

        self.resources_by_tool = {}
        self.resources_by_tool['shovel'] = {
            'default': {
                'minecraft:snowball': 1,
                'minecraft:gravel': 0.4,
                'minecraft:flint': 0.2,
            },
            'minecraft:looting': {
                'minecraft:flint': 0.4,
                'minecraft:gravel': 0.2,
            },
            'minecraft:silk_touch': {
                'minecraft:snow_block': 1,
                'minecraft:gravel': 0.5,
            }
        }

        self.resources_by_tool['pickaxe'] = {
            'minecraft:silk_touch': {
                'minecraft:ice': 1,
                'minecraft:packed_ice': 1,
                'minecraft:blue_ice': 0.5,
                'minecraft:magma_block': 0.2,
            }
        }
        
        self.resources_by_tool[self.fallback] = {
            'default': {
                'minecraft:gravel': 0.4,
                'minecraft:flint': 0.2,
            },
        }