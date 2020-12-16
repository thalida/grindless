from .savanna import Savanna

class SavannaPlateau(Savanna):
    def setup_region(self):
        super().setup_region()
        self.name = 'savanna_plateau'
        self.display_name = 'Savanna Plateau'
