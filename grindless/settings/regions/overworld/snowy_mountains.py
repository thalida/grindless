from .snowy_tundra import SnowyTundra

class SnowyMountains(SnowyTundra):
    def __init__(self):
        super().__init__()
        self.name = 'snowy_mountains'
        self.display_name = 'Snowy Mountains'