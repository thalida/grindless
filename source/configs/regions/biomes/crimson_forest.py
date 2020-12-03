from ..base_region import BaseRegion

class CrimsonForest(BaseRegion):
    def __init__(self):
        self.name = 'crimson_forest'
        self.display_name = 'Crimson Forest'

        self.items = {
                'minecraft:crimson_stem': 1,
                'minecraft:netherrack': 1,
                'minecraft:blackstone': 0.5,
                'minecraft:crimson_nylium': 1,
                'minecraft:soul_sand': 1,
                'minecraft:nether_wart_block': 1,
                'minecraft:shroomlight': 0.5,
                'minecraft:crimson_roots': 0.5,
                'minecraft:crimson_fungus': 0.5,
                'minecraft:warped_fungus': 0.4,
                'minecraft:weeping_vines': 0.2,
        }

        self.resources_by_tool = {}
        self.resources_by_tool['axe'] = {
            'default': {
                'minecraft:crimson_stem': 1,
            }
        }

        self.resources_by_tool['pickaxe'] = {
            'default': {
                'minecraft:netherrack': 1,
                'minecraft:blackstone': 0.5,
            },
            'minecraft:silk_touch': {
                'minecraft:crimson_nylium': 1,
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
                'minecraft:nether_wart_block': 1,
                'minecraft:shroomlight': 0.5,
                'minecraft:crimson_roots': 0.5,
                'minecraft:crimson_fungus': 0.5,
                'minecraft:warped_fungus': 0.4,
            }
        }
        
        self.resources_by_tool['shears'] = {
            'default': {
                'minecraft:crimson_roots': 0.5,
                'minecraft:crimson_fungus': 0.5,
                'minecraft:warped_fungus': 0.4,
                'minecraft:weeping_vines': 0.2,
            }
        }
        
        self.resources_by_tool[self.fallback] = {
            'default': {
                'minecraft:netherrack': 1,
                'minecraft:crimson_stem': 1,
                'minecraft:shroomlight': 0.5,
                'minecraft:crimson_roots': 0.5,
                'minecraft:crimson_fungus': 0.5,
                'minecraft:warped_fungus': 0.4,
            },
            'minecraft:silk_touch': {
                'minecraft:weeping_vines': 0.2,
            }
        }