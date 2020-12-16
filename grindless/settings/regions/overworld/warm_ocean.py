from .ocean import Ocean

class WarmOcean(Ocean):
    def setup_region(self):
        self.name = 'warm_ocean'
        self.display_name = 'Warm Ocean'

        self.items = {
            'minecraft:sea_pickle': 0.3,
            'minecraft:sand': 2,
            'minecraft:dirt': 2,
            'minecraft:gravel': 1,
            'minecraft:flint': 1,
            'minecraft:clay': 0.5,
            'minecraft:clay_ball': 0.5,
            'minecraft:kelp': 2,
            'minecraft:seagrass': 2,
            'minecraft:tube_coral_block': 4,
            'minecraft:brain_coral_block': 4,
            'minecraft:bubble_coral_block': 4,
            'minecraft:fire_coral_block': 4,
            'minecraft:horn_coral_block': 4,
            'minecraft:tube_coral': 2,
            'minecraft:brain_coral': 2,
            'minecraft:bubble_coral': 2,
            'minecraft:fire_coral': 2,
            'minecraft:horn_coral': 2,
            'minecraft:tube_coral_fan': 2,
            'minecraft:brain_coral_fan': 2,
            'minecraft:bubble_coral_fan': 2,
            'minecraft:fire_coral_fan': 2,
            'minecraft:horn_coral_fan': 2,
        }
