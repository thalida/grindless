from .badlands_plateau import BadlandsPlateau

class WoodedBadlandsPlateau(BadlandsPlateau):
    def __init__(self):
        super().__init__()
        self.name = 'wooded_badlands_plateau'
        self.display_name = 'Wooded Badlands Plateau'

        