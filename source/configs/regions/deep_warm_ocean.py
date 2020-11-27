from .ocean import DeepOcean

class DeepWarmOcean(DeepOcean):
    def __init__(self):
        super().__init__()
        self.name = 'deep_warm_ocean'
        self.display_name = 'Deep Warm Ocean'