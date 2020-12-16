from .swamp import Swamp

class SwampHills(Swamp):
    def setup_region(self):
        super().setup_region()
        self.name = 'swamp_hills'
        self.display_name = 'Swamp Hills'
