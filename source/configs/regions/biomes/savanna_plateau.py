from .savanna import Savanna

class SavannaPlateau(Savanna):
    def __init__(self):
        super().__init__()
        self.name = 'savanna_plateau'
        self.display_name = 'Savanna Plateau'