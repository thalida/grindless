from .snowy_taiga import SnowyTaiga

class SnowyTaigaMountains(SnowyTaiga):
    def __init__(self):
        super().__init__()
        self.name = 'snowy_taiga_mountains'
        self.display_name = 'Snowy Taiga Mountains'
        