from .taiga import SnowyTaiga

class SnowyTaigaHills(SnowyTaiga):
    def __init__(self):
        super().__init__()
        self.name = 'snowy_taiga_hills'
        self.display_name = 'Snowy Taiga Hills'
        