from .ocean import Ocean

class ColdOcean(Ocean):
    def setup_region(self):
        super().setup_region()
        self.name = 'cold_ocean'
        self.display_name = 'Cold Ocean'
