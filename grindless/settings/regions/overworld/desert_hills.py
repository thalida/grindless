from .desert import Desert

class DesertHills(Desert):
    def __init__(self):
        super().__init__()
        self.name = 'desert_hills'
        self.display_name = 'Desert Hills'
        