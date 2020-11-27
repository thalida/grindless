from .ocean import DeepOcean

class DeepColdOcean(DeepOcean):
    def __init__(self):
        super().__init__()
        self.name = 'deep_cold_ocean'
        self.display_name = 'Deep Cold Ocean'