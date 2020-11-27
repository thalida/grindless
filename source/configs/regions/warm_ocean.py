from .ocean import Ocean

class WarmOcean(Ocean):
    def __init__(self):
        self.name = 'warm_ocean'
        self.display_name = 'Warm Ocean'

        self.resources_by_tool = {}
        self.resources_by_tool['shovel'] = {
            'default': {
                'items': {
                    'minecraft:sea_pickle': 0.3,
                    'minecraft:sand': 0.4,
                    'minecraft:dirt': 0.4,
                    'minecraft:gravel': 0.2,
                    'minecraft:fint': 0.1,
                    'minecraft:clay_ball': 0.2,
                },
                'damage': 0.25
            },
            'minecraft:looting': {
                'items': {
                    'minecraft:sand': 0.5,
                    'minecraft:dirt': 0.4,
                    'minecraft:flint': 0.2,
                    'minecraft:gravel': 0.1,
                    'minecraft:clay_ball': 0.2,
                }
            },
            'minecraft:silk_touch': {
                'items': {
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
            },
            'minecraft:unbreaking': {
                'damage': 0.125
            }
        }

        self.resources_by_tool['pickaxe'] = {
            'default': {
                'items': {},
                'damage': 0
            },
            'minecraft:unbreaking': {
                'damage': 0.75
            },
            'minecraft:silk_touch': {
                'items': {
                    'minecraft:tube_coral_block': 0.5,
                    'minecraft:brain_coral_block': 0.5,
                    'minecraft:bubble_coral_block': 0.5,
                    'minecraft:fire_coral_block': 0.5,
                    'minecraft:horn_coral_block': 0.5,
                },
                'damage': 0.25
            }
        }

        self.resources_by_tool['shears'] = {
            'default': {
                'items': {
                    "minecraft:kelp": 1,
                    "minecraft:seagrass": 1,
                },
                'damage': 1.5
            },
            'minecraft:unbreaking': {
                'damage': 0.75
            }
        }
        
        self.resources_by_tool[self.fallback] = self.resources_by_tool['shovel']