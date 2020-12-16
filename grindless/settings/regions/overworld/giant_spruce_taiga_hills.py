from .giant_spruce_taiga import GiantSpruceTaiga

class GiantSpruceTaigaHills(GiantSpruceTaiga):
    def setup_region(self):
        super().setup_region()
        self.name = 'giant_spruce_taiga_hills'
        self.display_name = 'Giant Spruce Taiga Hills'
