from .deep_ocean import DeepOcean

class DeepColdOcean(DeepOcean):
    def setup_region(self):
        super().setup_region()
        self.name = 'deep_cold_ocean'
        self.display_name = 'Deep Cold Ocean'
