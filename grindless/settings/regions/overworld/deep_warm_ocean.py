from .deep_ocean import DeepOcean

class DeepWarmOcean(DeepOcean):
    def setup_region(self):
        super().setup_region()
        self.name = 'deep_warm_ocean'
        self.display_name = 'Deep Warm Ocean'
