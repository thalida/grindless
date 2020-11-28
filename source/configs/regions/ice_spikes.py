from .base_region import BaseRegion

class IceSpikes(BaseRegion):
    def __init__(self):
        self.name = 'ice_spikes'
        self.display_name = 'Ice Spikes'

        self.resources_by_tool = {}
        self.resources_by_tool['shovel'] = {
            'default': {
                'minecraft:snowball': 1,
                'minecraft:dirt': 0.1,
            },
            'minecraft:silk_touch': {
                'minecraft:snow_block': 2,
            }
        }

        self.resources_by_tool['pickaxe'] = {
            'minecraft:silk_touch': {
                'minecraft:ice': 0.5,
                'minecraft:packed_ice': 1,
            }
        }
        
        self.resources_by_tool[self.fallback] = self.resources_by_tool['shovel']