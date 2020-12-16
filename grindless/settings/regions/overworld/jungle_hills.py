from .jungle import Jungle

class JungleHills(Jungle):
    def setup_region(self):
        super().setup_region()
        self.name = 'jungle_hills'
        self.display_name = 'Jungle Hills'
