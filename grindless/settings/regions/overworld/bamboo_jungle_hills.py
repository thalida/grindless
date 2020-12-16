from .bamboo_jungle import BambooJungle

class BambooJungleHills(BambooJungle):
    def setup_region(self):
        super().setup_region()
        self.name = 'bamboo_jungle_hills'
        self.display_name = 'Bamboo Jungle Hills'
