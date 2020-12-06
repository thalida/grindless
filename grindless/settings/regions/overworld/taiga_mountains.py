from .taiga import Taiga

class TaigaMountains(Taiga):
    def __init__(self):
        super().__init__()
        self.name = 'taiga_mountains'
        self.display_name = 'Taiga Mountains'
        