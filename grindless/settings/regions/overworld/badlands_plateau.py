from .badlands import Badlands

class BadlandsPlateau(Badlands):
    def __init__(self):
        super().__init__()
        self.name = 'badlands_plateau'
        self.display_name = 'Badlands Plateau'