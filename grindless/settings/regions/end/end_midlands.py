from .the_end import TheEnd

class EndMidlands(TheEnd):
    def setup_region(self):
        super().setup_region()
        self.name = 'end_midlands'
        self.display_name = 'End Midlands'
