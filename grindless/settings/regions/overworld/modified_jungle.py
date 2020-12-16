from .jungle import Jungle

class ModifiedJungle(Jungle):
    def setup_region(self):
        super().setup_region()
        self.name = 'modified_jungle'
        self.display_name = 'Modified Jungle'
