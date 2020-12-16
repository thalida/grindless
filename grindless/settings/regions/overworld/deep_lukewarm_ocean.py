from .deep_ocean import DeepOcean

class DeepLukewarmOcean(DeepOcean):
    def setup_region(self):
        super().setup_region()
        self.name = 'deep_lukewarm_ocean'
        self.display_name = 'Deep Lukewarm Ocean'
