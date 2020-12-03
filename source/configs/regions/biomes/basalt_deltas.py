from ..base_region import BaseRegion

class BasaltDeltas(BaseRegion):
    def __init__(self):
        self.name = 'basalt_deltas'
        self.display_name = 'Basalt Deltas'
        self.items = {
            'minecraft:netherrack': 2,
            'minecraft:basalt': 2,
            'minecraft:blackstone': 1,
            'minecraft:magma_block': 1,
        }

        self.resources_by_tool = {}
        self.resources_by_tool['pickaxe'] = {
            'default': {
                'minecraft:netherrack': 1,
                'minecraft:basalt': 0.5,
                'minecraft:blackstone': 0.5,
            },
            'minecraft:silk_touch': {
                'minecraft:magma_block': 0.2,
            }
        }
        
        self.resources_by_tool[self.fallback] = {
            'default': {
                'minecraft:netherrack': 1,
            }
        }
