from .ocean import Ocean

class DeepFrozenOcean(Ocean):
    def setup_region(self):
        self.name = 'deep_frozen_ocean'
        self.display_name = 'Deep Frozen Ocean'

        self.items = {
            'minecraft:snowball': 1,
            'minecraft:gravel': 0.5,
            'minecraft:flint': 0.5,
            'minecraft:snow_block': 1,
            'minecraft:ice': 1,
            'minecraft:packed_ice': 1,
            'minecraft:blue_ice': 0.5,
            'minecraft:magma_block': 0.2,
        }
