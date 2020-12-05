from .birch_forest import BirchForest

class BirchForestHills(BirchForest):
    def __init__(self):
        super().__init__()
        self.name = 'birch_forest_hills'
        self.display_name = 'Birch Forest Hills'
        