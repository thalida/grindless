from .snowy_taiga import SnowyTaiga

class SnowyTaigaMountains(SnowyTaiga):
    def setup_region(self):
        super().setup_region()
        self.name = 'snowy_taiga_mountains'
        self.display_name = 'Snowy Taiga Mountains'
