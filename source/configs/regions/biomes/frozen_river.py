from .river import River

class FrozenRiver(River):
    def __init__(self):
        self.name = 'frozen_river'
        self.display_name = 'Frozen River'

        self.items = {
                'minecraft:dirt': 0.5,
                'minecraft:clay_ball': 0.25,
                'minecraft:sand': 0.25,
                'minecraft:gravel': 0.25,
                'minecraft:flint': 0.125,
        }

        self.resources_by_tool = {}
        self.resources_by_tool['shovel'] = {
            'default': {
                'minecraft:dirt': 0.5,
                'minecraft:clay_ball': 0.25,
                'minecraft:sand': 0.25,
                'minecraft:gravel': 0.25,
                'minecraft:flint': 0.125,
            },
            'minecraft:fortune': {
                'minecraft:dirt': 0.5,
                'minecraft:clay_ball': 0.25,
                'minecraft:sand': 0.25,
                'minecraft:flint': 0.25,
                'minecraft:gravel': 0.125,
            },
            'minecraft:silk_touch': {
                'minecraft:grass_block': 0.5,
                'minecraft:clay': 0.25,
                'minecraft:sand': 0.25,
                'minecraft:gravel': 0.25,
            }
        }
        
        self.resources_by_tool['pickaxe'] = {
            'minecraft:silk_touch': {
                'minecraft:ice': 1,
            }
        }
        
        self.resources_by_tool[self.fallback] = self.resources_by_tool['shovel']