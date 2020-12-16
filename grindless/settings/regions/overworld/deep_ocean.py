from .ocean import Ocean

class DeepOcean(Ocean):
    def setup_region(self):
        self.name = 'deep_ocean'
        self.display_name = 'Deep Ocean'

        self.items = {
            'minecraft:sand': 1,
            'minecraft:gravel': 0.5,
            'minecraft:flint': 0.2,
            'minecraft:kelp': 1,
            'minecraft:seagrass': 2,
            'minecraft:magma_block': 0.2,
        }
