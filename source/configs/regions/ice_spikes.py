from .base_region import BaseRegion

class IceSpikes(BaseRegion):
    def __init__(self):
        self.name = 'ice_spikes'
        self.display_name = 'Ice Spikes'

        self.resources_by_tool = {}
        self.resources_by_tool['shovel'] = {
            'default': {
                'items': {
                    'minecraft:snowball': 1,
                    'minecraft:dirt': 0.1,
                },
                'damage': 0.25
            },
            'minecraft:silk_touch': {
                'items': {
                    'minecraft:snow_block': 2,
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
                    'minecraft:ice': 0.5,
                    'minecraft:packed_ice': 1,
                },
                'damage': 0.25
            }
        }
        
        self.resources_by_tool[self.fallback] = self.resources_by_tool['shovel']