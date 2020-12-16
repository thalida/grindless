from .snowy_taiga import SnowyTaiga

class SnowyTaigaHills(SnowyTaiga):
    def setup_region(self):
        super().setup_region()
        self.name = 'snowy_taiga_hills'
        self.display_name = 'Snowy Taiga Hills'
