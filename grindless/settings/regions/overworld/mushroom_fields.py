from ..base_region import BaseRegion

class MushroomFields(BaseRegion):
    def setup_region(self):
        self.name = 'mushroom_fields'
        self.display_name = 'Mushroom Fields'

        self.items = {
            'minecraft:mycelium': 4,
            'minecraft:brown_mushroom_block': 4,
            'minecraft:red_mushroom_block': 4,
            'minecraft:mushroom_stem': 2,
            'minecraft:red_mushroom': 2,
            'minecraft:brown_mushroom': 2,
            'minecraft:dirt': 1,
        }
