from .taiga import Taiga

class TaigaHills(Taiga):
    def setup_region(self):
        super().setup_region()
        self.name = 'taiga_hills'
        self.display_name = 'Taiga Hills'
