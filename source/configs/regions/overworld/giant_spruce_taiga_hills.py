from .giant_spruce_taiga import GiantSpruceTaiga

class GiantSpruceTaigaHills(GiantSpruceTaiga):
    def __init__(self):
        super().__init__()
        self.name = 'giant_spruce_taiga_hills'
        self.display_name = 'Giant Spruce Taiga Hills'
        