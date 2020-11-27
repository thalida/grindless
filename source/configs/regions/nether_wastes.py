from .base_region import BaseRegion

class NetherWastes(BaseRegion):
    def __init__(self):
        self.name = 'nether_wastes'
        self.display_name = 'Nether Wastes'

        self.resources_by_tool = {}
        self.resources_by_tool['pickaxe'] = {
            'default': {
                'items': {
                    'minecraft:netherrack': 1,
                    'minecraft:quartz': 0.5,
                    'minecraft:gold_nugget': 0.5,
                    'minecraft:magma_block': 0.4,
                    'minecraft:blackstone': 0.2,
                    'minecraft:glowstone_dust': 0.5,
                },
                'damage': 0.25
            },
            'minecraft:silk_touch': {
                'items': {
                    'minecraft:glowstone': 1,
                    'minecraft:nether_quartz_ore': 0.8,
                    'minecraft:nether_gold_ore': 0.4,
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
        
        self.resources_by_tool[self.fallback] = {
            'default': {
                'items': {
                    'minecraft:netherrack': 1,
                    'minecraft:soul_sand': 0.5,
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

        self.material_addons['diamond_pickaxe'] = {
            'default': {
                'items': {
                    'minecraft:netherite': 0.1,
                }
            }
        }
        self.material_addons['netherite_pickaxe'] = self.material_addons['diamond_pickaxe']
