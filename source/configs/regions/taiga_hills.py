from .taiga import Taiga

class TaigaHills(Taiga):
    def __init__(self):
        super().__init__()
        self.name = 'taiga_hills'
        self.display_name = 'Taiga Hills'
        