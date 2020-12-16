from .taiga import Taiga

class TaigaMountains(Taiga):
    def setup_region(self):
        super().setup_region()
        self.name = 'taiga_mountains'
        self.display_name = 'Taiga Mountains'
