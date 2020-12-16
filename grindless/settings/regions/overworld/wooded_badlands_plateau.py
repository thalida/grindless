from .badlands_plateau import BadlandsPlateau

class WoodedBadlandsPlateau(BadlandsPlateau):
    def setup_region(self):
        super().setup_region()
        self.name = 'wooded_badlands_plateau'
        self.display_name = 'Wooded Badlands Plateau'
