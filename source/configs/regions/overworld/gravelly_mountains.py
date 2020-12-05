from ..base_region import BaseRegion

class GravellyMountains(BaseRegion):
    def __init__(self):
        self.name = 'gravelly_mountains'
        self.display_name = 'Gravelly Mountains'

        self.items = {
            'minecraft:gravel': 4,
            'minecraft:flint': 4,
            'minecraft:stone': 2,
            'minecraft:cobblestone': 2,
        }