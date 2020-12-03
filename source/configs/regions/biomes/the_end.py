from ..base_region import BaseRegion

class TheEnd(BaseRegion):
    def __init__(self):
        self.name = 'the_end'
        self.display_name = 'The End'

        self.items = {
            'minecraft:end_stone': 4,
            'minecraft:shulker_shell': 4,
            'minecraft:elytra': 0.5,
            'minecraft:chorus_fruit': 2,
            'minecraft:chorus_flower': 1,
        }