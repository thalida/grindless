from .desert import Desert

class DesertHills(Desert):
    def setup_region(self):
        super().setup_region()
        self.name = 'desert_hills'
        self.display_name = 'Desert Hills'
