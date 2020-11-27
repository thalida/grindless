from .ocean import DeepOcean

class DeepLukewarmOcean(DeepOcean):
    def __init__(self):
        super().__init__()
        self.name = 'deep_lukewarm_ocean'
        self.display_name = 'Deep Lukewarm Ocean'