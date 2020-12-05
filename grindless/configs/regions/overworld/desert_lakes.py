from .desert import Desert

class DesertLakes(Desert):
    def __init__(self):
        super().__init__()
        self.name = 'desert_lakes'
        self.display_name = 'Desert Lakes'
        