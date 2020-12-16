from .the_end import TheEnd

class EndHighlands(TheEnd):
    def setup_region(self):
        super().setup_region()
        self.name = 'end_highlands'
        self.display_name = 'End Highlands'
