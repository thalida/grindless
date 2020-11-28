from .ocean import Ocean

class FrozenOcean(Ocean):
    def __init__(self):
        self.name = 'frozen_ocean'
        self.display_name = 'Frozen Ocean'

        self.resources_by_tool = {}
        self.resources_by_tool['shovel'] = {
            'default': {
                'minecraft:snowball': 1,
                'minecraft:sand': 0.5,
                'minecraft:gravel': 0.4,
                'minecraft:flint': 0.2,
                'minecraft:clay_ball': 0.2,
                'minecraft:dirt': 0.1,
            },
            'minecraft:fortune': {
                'minecraft:sand': 1,
                'minecraft:flint': 0.4,
                'minecraft:gravel': 0.2,
                'minecraft:clay_ball': 0.2,
                'minecraft:dirt': 0.1,
            },
            'minecraft:silk_touch': {
                'minecraft:snow_block': 1,
                'minecraft:sand': 1,
                'minecraft:gravel': 0.5,
                'minecraft:clay': 0.2,
                'minecraft:dirt': 0.1,
            }
        }

        self.resources_by_tool['pickaxe'] = {
            'minecraft:silk_touch': {
                'minecraft:ice': 1,
                'minecraft:packed_ice': 1,
                'minecraft:blue_ice': 0.5,
            }
        }
        
        self.resources_by_tool[self.fallback] = {
            'default': {
                'minecraft:sand': 1,
                'minecraft:gravel': 0.4,
                'minecraft:flint': 0.2,
                'minecraft:clay_ball': 0.2,
                'minecraft:dirt': 0.1,
            },
        }