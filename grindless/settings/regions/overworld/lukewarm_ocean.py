from .ocean import Ocean

class LukewarmOcean(Ocean):
    def setup_region(self):
        super().setup_region()
        self.name = 'lukewarm_ocean'
        self.display_name = 'Lukewarm Ocean'
