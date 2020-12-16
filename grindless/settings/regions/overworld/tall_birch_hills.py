from .birch_forest import BirchForest

class TallBirchHills(BirchForest):
    def setup_region(self):
        super().setup_region()
        self.name = 'tall_birch_hills'
        self.display_name = 'Tall Birch Hills'
