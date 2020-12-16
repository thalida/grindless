from .badlands import Badlands

class ErodedBadlands(Badlands):
    def setup_region(self):
        super().setup_region()
        self.name = 'eroded_badlands'
        self.display_name = 'Eroded Badlands'
