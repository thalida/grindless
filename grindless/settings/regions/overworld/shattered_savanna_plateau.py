from .shattered_savanna import ShatteredSavanna

class ShatteredSavannaPlateau(ShatteredSavanna):
    def setup_region(self):
        super().setup_region()
        self.name = 'shattered_savanna_plateau'
        self.display_name = 'Shattered Savanna Plateau'
