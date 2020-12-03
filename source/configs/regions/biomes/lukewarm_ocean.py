from .ocean import Ocean

class LukewarmOcean(Ocean):
    def __init__(self):
        super().__init__()
        self.name = 'lukewarm_ocean'
        self.display_name = 'Lukewarm Ocean'