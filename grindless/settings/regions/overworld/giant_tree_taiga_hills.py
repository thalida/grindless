from .giant_tree_taiga import GiantTreeTaiga

class GiantTreeTaigaHills(GiantTreeTaiga):
    def setup_region(self):
        super().setup_region()
        self.name = 'giant_tree_taiga_hills'
        self.display_name = 'Giant Tree Taiga Hills'
