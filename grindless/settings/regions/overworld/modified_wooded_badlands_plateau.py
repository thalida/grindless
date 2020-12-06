from .modified_badlands_plateau import ModifiedBadlandsPlateau

class ModifiedWoodedBadlandsPlateau(ModifiedBadlandsPlateau):
    def __init__(self):
        super().__init__()
        self.name = 'modified_wooded_badlands_plateau'
        self.display_name = 'Modified Wooded Badlands Plateau'