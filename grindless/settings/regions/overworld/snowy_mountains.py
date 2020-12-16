from .snowy_tundra import SnowyTundra

class SnowyMountains(SnowyTundra):
    def setup_region(self):
        super().setup_region()
        self.name = 'snowy_mountains'
        self.display_name = 'Snowy Mountains'
