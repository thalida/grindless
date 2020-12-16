from .forest import Forest

class WoodedHills(Forest):
    def setup_region(self):
        super().setup_region()
        self.name = 'wooded_hills'
        self.display_name = 'Wooded Hills'
