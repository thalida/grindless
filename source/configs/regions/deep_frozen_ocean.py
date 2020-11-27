from .ocean import Ocean

class DeepFrozenOcean(Ocean):
    def __init__(self):
        self.name = 'deep_frozen_ocean'
        self.display_name = 'Deep Frozen Ocean'

        self.resources_by_tool = {}
        self.resources_by_tool['shovel'] = {
            'default': {
                'items': {
                    'minecraft:snowball': 1,
                    'minecraft:gravel': 0.4,
                    'minecraft:fint': 0.2,
                },
                'damage': 0.25
            },
            'minecraft:looting': {
                'items': {
                    'minecraft:flint': 0.4,
                    'minecraft:gravel': 0.2,
                }
            },
            'minecraft:silk_touch': {
                'items': {
                    'minecraft:snow_block': 1,
                    'minecraft:gravel': 0.5,
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
                    'minecraft:magma_block': 0.2,
                },
                'damage': 0.25
            }
        }
        
        self.resources_by_tool[self.fallback] = {
            'default': {
                'items': {
                    'minecraft:gravel': 0.4,
                    'minecraft:fint': 0.2,
                },
                'damage': 0.25
            },
            'minecraft:unbreaking': {
                'damage': 0.125
            }
        }