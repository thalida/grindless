from .plains import Plains

class SunflowerPlains(Plains):
    def setup_region(self):
        super().setup_region()
        self.name = 'sunflower_plains'
        self.display_name = 'Sunflower Plains'

        self.items = {
            'minecraft:oak_log': 1,
            'minecraft:oak_leaves': 1,
            'minecraft:oak_sapling': 0.5,
            'minecraft:stick': 0.5,
            'minecraft:apple': 0.25,
            "minecraft:grass": 2,
            "minecraft:grass_block": 4,
            "minecraft:dirt": 2,
            "minecraft:wheat_seeds": 2,
            "minecraft:sunflower": 4,
            "minecraft:azure_bluet": 0.25,
            "minecraft:oxeye_daisy": 0.25,
            "minecraft:cornflower": 0.25,
        }
