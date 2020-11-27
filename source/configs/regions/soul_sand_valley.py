from .base_region import BaseRegion

class SoulSandValley(BaseRegion):
    def __init__(self):
        self.name = 'soul_sand_valley'
        self.display_name = 'Soul Sand Valley'

        self.resources_by_tool = {}
        self.resources_by_tool['pickaxe'] = {
            'default': {
                'items': {
                    'minecraft:netherrack': 1,
                    'minecraft:basalt': 0.5,
                    'minecraft:blackstone': 0.5,
                    'minecraft:glowstone_dust': 0.5,
                },
                'damage': 0.25
            },
            'minecraft:silk_touch': {
                'items': {
                    'minecraft:glowstone': 1,
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
                    'minecraft:soul_soil': 0.5,
                    'minecraft:gravel': 0.5,
                    'minecraft:flint': 0.2,
                },
                'damage': 0.25
            },
            'minecraft:looting': {
                'items': {
                    'minecraft:soul_sand': 1,
                    'minecraft:soul_soil': 0.5,
                    'minecraft:flint': 0.5,
                    'minecraft:gravel': 0.2,
                }
            },
            'minecraft:silk_touch': {
                'items': {
                    'minecraft:soul_sand': 1,
                    'minecraft:soul_soil': 0.5,
                    'minecraft:gravel': 0.5,
                }
            },
            'minecraft:unbreaking': {
                'damage': 0.125
            }
        }
        
        self.resources_by_tool['hoe'] = {
            'default': {
                'items': {
                    'minecraft:crimson_roots': 0.5,
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
                    'minecraft:crimson_roots': 0.5,
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
                    'minecraft:soul_sand': 0.5,
                    'minecraft:soul_soil': 0.5,
                    'minecraft:gravel': 0.5,
                    'minecraft:flint': 0.2,
                    'minecraft:crimson_roots': 0.2,
                },
                'damage': 0.25
            },
            'minecraft:unbreaking': {
                'damage': 0.125
            }
        }
