from .the_end import TheEnd

class EndBarrens(TheEnd):
    def setup_region(self):
        super().setup_region()
        self.name = 'end_barrens'
        self.display_name = 'End Barrens'
