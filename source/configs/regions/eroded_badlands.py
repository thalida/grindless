from .badlands import Badlands

class ErodedBadlands(Badlands):
    def __init__(self):
        super().__init__()
        self.name = 'eroded_badlans'
        self.display_name = 'Eroded Badlands'