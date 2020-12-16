from .birch_forest import BirchForest

class BirchForestHills(BirchForest):
    def setup_region(self):
        super().setup_region()
        self.name = 'birch_forest_hills'
        self.display_name = 'Birch Forest Hills'
