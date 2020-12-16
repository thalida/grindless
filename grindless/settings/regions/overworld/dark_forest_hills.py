from .dark_forest import DarkForest

class DarkForestHills(DarkForest):
    def setup_region(self):
        super().setup_region()
        self.name = 'dark_forest_hills'
        self.display_name = 'Dark Forest Hills'
