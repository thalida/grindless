from .mountains import Mountains

class WoodedMountains(Mountains):
    def setup_region(self):
        super().setup_region()
        self.name = 'wooded_mountains'
        self.display_name = 'Wooded Mountains'
