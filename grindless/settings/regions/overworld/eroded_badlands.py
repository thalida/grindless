from .badlands import Badlands

class ErodedBadlands(Badlands):
    def __init__(self):
        super().__init__()
        self.name = 'eroded_badlands'
        self.display_name = 'Eroded Badlands'