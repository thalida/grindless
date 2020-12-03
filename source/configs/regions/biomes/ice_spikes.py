from ..base_region import BaseRegion

class IceSpikes(BaseRegion):
    def __init__(self):
        self.name = 'ice_spikes'
        self.display_name = 'Ice Spikes'

        self.items = {
            'minecraft:ice': 2,
            'minecraft:packed_ice': 2,
            'minecraft:snowball': 2,
            'minecraft:snow_block': 2,
            'minecraft:dirt': 0.5,
        }