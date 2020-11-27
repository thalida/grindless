from .base_region import BaseRegion

class BasaltDeltas(BaseRegion):
    def __init__(self):
        self.name = 'basalt_deltas'
        self.display_name = 'Basalt Deltas'

        self.resources_by_tool = {}
        self.resources_by_tool['pickaxe'] = {
            'default': {
                'items': {
                    'minecraft:netherrack': 1,
                    'minecraft:basalt': 0.5,
                    'minecraft:blackstone': 0.5,
                },
                'damage': 0.25
            },
            'minecraft:silk_touch': {
                'items': {
                    'minecraft:magma_block': 0.2,
                }
            },
            'minecraft:unbreaking': {
                'damage': 0.125
            }
        }
        
        self.resources_by_tool[self.fallback] = {
            'default': {
                'items': {
                    'minecraft:netherrack': 1,
                },
                'damage': 0.25
            },
            'minecraft:unbreaking': {
                'damage': 0.125
            }
        }
