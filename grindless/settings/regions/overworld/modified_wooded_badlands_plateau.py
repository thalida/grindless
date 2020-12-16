from .modified_badlands_plateau import ModifiedBadlandsPlateau

class ModifiedWoodedBadlandsPlateau(ModifiedBadlandsPlateau):
    def setup_region(self):
        super().setup_region()
        self.name = 'modified_wooded_badlands_plateau'
        self.display_name = 'Modified Wooded Badlands Plateau'
