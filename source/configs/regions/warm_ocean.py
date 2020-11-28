from .ocean import Ocean

class WarmOcean(Ocean):
    def __init__(self):
        self.name = 'warm_ocean'
        self.display_name = 'Warm Ocean'

        self.resources_by_tool = {}
        self.resources_by_tool['shovel'] = {
            'default': {
                'minecraft:sea_pickle': 0.3,
                'minecraft:sand': 0.4,
                'minecraft:dirt': 0.4,
                'minecraft:gravel': 0.2,
                'minecraft:flint': 0.1,
                'minecraft:clay_ball': 0.2,
            },
            'minecraft:looting': {
                'minecraft:sand': 0.5,
                'minecraft:dirt': 0.4,
                'minecraft:flint': 0.2,
                'minecraft:gravel': 0.1,
                'minecraft:clay_ball': 0.2,
            },
            'minecraft:silk_touch': {
                'minecraft:sand': 0.5,
                'minecraft:dirt': 0.4,
                'minecraft:gravel': 0.3,
                'minecraft:clay': 0.2,
                'minecraft:tube_coral': 0.2,
                'minecraft:brain_coral': 0.2,
                'minecraft:bubble_coral': 0.2,
                'minecraft:fire_coral': 0.2,
                'minecraft:horn_coral': 0.2,
                'minecraft:tube_coral_fan': 0.2,
                'minecraft:brain_coral_fan': 0.2,
                'minecraft:bubble_coral_fan': 0.2,
                'minecraft:fire_coral_fan': 0.2,
                'minecraft:horn_coral_fan': 0.2,
            }
        }

        self.resources_by_tool['pickaxe'] = {
            'minecraft:silk_touch': {
                'minecraft:tube_coral_block': 0.5,
                'minecraft:brain_coral_block': 0.5,
                'minecraft:bubble_coral_block': 0.5,
                'minecraft:fire_coral_block': 0.5,
                'minecraft:horn_coral_block': 0.5,
            }
        }

        self.resources_by_tool['shears'] = {
            'default': {
                "minecraft:kelp": 1,
                "minecraft:seagrass": 1,
            }
        }
        
        self.resources_by_tool[self.fallback] = self.resources_by_tool['shovel']