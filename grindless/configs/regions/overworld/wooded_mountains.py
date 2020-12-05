from .mountains import Mountains

class WoodedMountains(Mountains):
    def __init__(self):
        super().__init__()
        self.name = 'wooded_mountains'
        self.display_name = 'Wooded Mountains'
        