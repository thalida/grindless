from .base_region import BaseRegion

class WarpedForest(BaseRegion):
    def __init__(self):
        self.name = 'warped_forest'
        self.display_name = 'Warped Forest'

        self.resources_by_tool = {}
        self.resources_by_tool['axe'] = {
            'default': {
                'items': {
                    'minecraft:warped_stem': 1,
                },
                'damage': 0.25
            },
            'minecraft:silk_touch': {
                'items': {}
            },
            'minecraft:unbreaking': {
                'damage': 0.125
            }
        }

        self.resources_by_tool['pickaxe'] = {
            'default': {
                'items': {
                    'minecraft:netherrack': 1,
                    'minecraft:blackstone': 0.5,
                },
                'damage': 0.25
            },
            'minecraft:silk_touch': {
                'items': {
                    'minecraft:warped_nylium': 1,
                    'minecraft:netherrack': 0.5,
                }
            },
            'minecraft:unbreaking': {
                'damage': 0.125
            }
        }
        
        self.resources_by_tool['shovel'] = {
            'default': {
                'items': {
                    'minecraft:soul_sand': 1,
                },
                'damage': 0.25
            },
            'minecraft:unbreaking': {
                'damage': 0.125
            }
        }
        
        self.resources_by_tool['hoe'] = {
            'default': {
                'items': {
                    'minecraft:warped_wart_block': 1,
                    'minecraft:shroom_light': 0.5,
                    'minecraft:warped_roots': 0.5,
                    'minecraft:crimson_fungus': 0.4,
                    'minecraft:warped_fungus': 0.5,
                },
                'damage': 0.25
            },
            'minecraft:unbreaking': {
                'damage': 0.125
            }
        }
        
        self.resources_by_tool['shears'] = {
            'default': {
                'items': {
                    'minecraft:warped_roots': 0.5,
                    'minecraft:crimson_fungus': 0.4,
                    'minecraft:warped_fungus': 0.5,
                    'minecraft:weeping_vines': 0.2,
                    'minecraft:nether_sprouts': 0.2,
                },
                'damage': 0.25
            },
            'minecraft:unbreaking': {
                'damage': 0.125
            }
        }
        
        self.resources_by_tool[self.fallback] = {
            'default': {
                'items': {
                    'minecraft:netherrack': 1,
                    'minecraft:crimson_stem': 1,
                    'minecraft:shroom_light': 0.5,
                    'minecraft:warped_roots': 0.5,
                    'minecraft:crimson_fungus': 0.4,
                    'minecraft:warped_fungus': 0.5,
                },
                'damage': 0.25
            },
            'minecraft:silk_touch': {
                'items': {
                    'minecraft:twisting_vines': 0.2,
                },
            }
            'minecraft:unbreaking': {
                'damage': 0.125
            }
        }