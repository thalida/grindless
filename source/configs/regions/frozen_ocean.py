from .ocean import Ocean

class FrozenOcean(Ocean):
    def __init__(self):
        self.name = 'frozen_ocean'
        self.display_name = 'Frozen Ocean'

        self.resources_by_tool = {}
        self.resources_by_tool['shovel'] = {
            'default': {
                'items': {
                    'minecraft:snowball': 1,
                    'minecraft:sand': 0.5,
                    'minecraft:gravel': 0.4,
                    'minecraft:flint': 0.2,
                    'minecraft:clay_ball': 0.2,
                    'minecraft:dirt': 0.1,
                },
                'damage': 0.25
            },
            'minecraft:looting': {
                'items': {
                    'minecraft:sand': 1,
                    'minecraft:flint': 0.4,
                    'minecraft:gravel': 0.2,
                    'minecraft:clay_ball': 0.2,
                    'minecraft:dirt': 0.1,
                }
            },
            'minecraft:silk_touch': {
                'items': {
                    'minecraft:snow_block': 1,
                    'minecraft:sand': 1,
                    'minecraft:gravel': 0.5,
                    'minecraft:clay': 0.2,
                    'minecraft:dirt': 0.1,
                }
            },
            'minecraft:unbreaking': {
                'damage': 0.125
            }
        }

        self.resources_by_tool['pickaxe'] = {
            'default': {
                'items': {},
                'damage': 0
            },
            'minecraft:unbreaking': {
                'damage': 0.75
            },
            'minecraft:silk_touch': {
                'items': {
                    'minecraft:ice': 1,
                    'minecraft:packed_ice': 1,
                    'minecraft:blue_ice': 0.5,
                },
                'damage': 0.25
            }
        }
        
        self.resources_by_tool[self.fallback] = {
            'default': {
                'items': {
                    'minecraft:sand': 1,
                    'minecraft:gravel': 0.4,
                    'minecraft:flint': 0.2,
                    'minecraft:clay_ball': 0.2,
                    'minecraft:dirt': 0.1,
                },
                'damage': 0.25
            },
            'minecraft:unbreaking': {
                'damage': 0.125
            }
        }