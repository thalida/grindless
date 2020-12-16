from .the_end import TheEnd

class SmallEndIslands(TheEnd):
    def setup_region(self):
        super().setup_region()
        self.name = 'small_end_islands'
        self.display_name = 'Small End Islands'
