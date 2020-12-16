from .desert import Desert

class DesertLakes(Desert):
    def setup_region(self):
        super().setup_region()
        self.name = 'desert_lakes'
        self.display_name = 'Desert Lakes'
