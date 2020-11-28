from .base_region import BaseRegion

class BambooJungle(BaseRegion):
    def __init__(self):
        self.name = 'bamboo_jungle'
        self.display_name = 'Bamboo Jungle'

        self.resources_by_tool = {}
        self.resources_by_tool['axe'] = {
            'default': {
                'minecraft:bamboo': 2,
                'minecraft:jungle_log': 1,
                'minecraft:jungle_sapling': 1,
                'minecraft:cocoa_beans': 0.4,
                'minecraft:melon_slice': 0.25,
            },
            'minecraft:silk_touch': {
                'minecraft:jungle_leaves': 2,
                'minecraft:melon': 0.25,
            },
        }

        self.resources_by_tool['sword'] = {
            'default': {
                "minecraft:bamboo": 2,
            }
        }

        self.resources_by_tool['shovel'] = {
            'default': {
                "minecraft:dirt": 1,
                "minecraft:wheat_seeds": 0.25,
            },
            'minecraft:silk_touch': {
                "minecraft:grass_block": 1,
                "minecraft:podzol": 0.8,
                "minecraft:wheat_seeds": 0.25,
            }
        }

        self.resources_by_tool['shears'] = {
            'default': {
                "minecraft:vine": 2,
                "minecraft:jungle_leaves": 2,
            }
        }
        
        self.resources_by_tool[self.fallback] = self.resources_by_tool['axe']