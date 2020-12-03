from ..base_region import BaseRegion

class WarpedForest(BaseRegion):
    def __init__(self):
        self.name = 'warped_forest'
        self.display_name = 'Warped Forest'

        self.items = {
                'minecraft:warped_stem': 1,
        }

        self.resources_by_tool = {}
        self.resources_by_tool['axe'] = {
            'default': {
                'minecraft:warped_stem': 1,
            }
        }

        self.resources_by_tool['pickaxe'] = {
            'default': {
                'minecraft:netherrack': 1,
                'minecraft:blackstone': 0.5,
            },
            'minecraft:silk_touch': {
                'minecraft:warped_nylium': 1,
                'minecraft:netherrack': 0.5,
            }
        }
        
        self.resources_by_tool['shovel'] = {
            'default': {
                'minecraft:soul_sand': 1,
            }
        }
        
        self.resources_by_tool['hoe'] = {
            'default': {
                'minecraft:warped_wart_block': 1,
                'minecraft:shroomlight': 0.5,
                'minecraft:warped_roots': 0.5,
                'minecraft:crimson_fungus': 0.4,
                'minecraft:warped_fungus': 0.5,
            }
        }
        
        self.resources_by_tool['shears'] = {
            'default': {
                'minecraft:warped_roots': 0.5,
                'minecraft:crimson_fungus': 0.4,
                'minecraft:warped_fungus': 0.5,
                'minecraft:weeping_vines': 0.2,
                'minecraft:nether_sprouts': 0.2,
            }
        }
        
        self.resources_by_tool[self.fallback] = {
            'default': {
                'minecraft:netherrack': 1,
                'minecraft:crimson_stem': 1,
                'minecraft:shroomlight': 0.5,
                'minecraft:warped_roots': 0.5,
                'minecraft:crimson_fungus': 0.4,
                'minecraft:warped_fungus': 0.5,
            },
            'minecraft:silk_touch': {
                'minecraft:twisting_vines': 0.2,
            }
        }