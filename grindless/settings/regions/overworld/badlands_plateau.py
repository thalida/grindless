from .badlands import Badlands

class BadlandsPlateau(Badlands):
    def setup_region(self):
        super().setup_region()
        self.name = 'badlands_plateau'
        self.display_name = 'Badlands Plateau'
