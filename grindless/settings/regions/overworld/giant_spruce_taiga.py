from .giant_tree_taiga import GiantTreeTaiga

class GiantSpruceTaiga(GiantTreeTaiga):
    def __init__(self):
        super().__init__()
        self.name = 'giant_spruce_taiga'
        self.display_name = 'Giant Spruce Taiga'
        