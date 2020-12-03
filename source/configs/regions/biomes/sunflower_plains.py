from .plains import Plains

class SunflowerPlains(Plains):
    def __init__(self):
        super().__init__()
        self.name = 'sunflower_plains'
        self.display_name = 'Sunflower Plains'

        self.items = {
                "minecraft:wheat_seeds": 1,
                "minecraft:sunflower": 0.8,
                "minecraft:azure_bluet": 0.25,
                "minecraft:oxeye_daisy": 0.25,
                "minecraft:cornflower": 0.25,
        }

        self.resources_by_tool['hoe'] = {
            'default': {
                "minecraft:wheat_seeds": 1,
                "minecraft:sunflower": 0.8,
                "minecraft:azure_bluet": 0.25,
                "minecraft:oxeye_daisy": 0.25,
                "minecraft:cornflower": 0.25,
            }
        }

        self.resources_by_tool[self.fallback] = self.resources_by_tool['hoe']