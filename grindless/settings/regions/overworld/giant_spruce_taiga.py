from .giant_tree_taiga import GiantTreeTaiga

class GiantSpruceTaiga(GiantTreeTaiga):
    def setup_region(self):
        super().setup_region()
        self.name = 'giant_spruce_taiga'
        self.display_name = 'Giant Spruce Taiga'
