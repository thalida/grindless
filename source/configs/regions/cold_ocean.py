from .ocean import Ocean

class ColdOcean(Ocean):
    def __init__(self):
        super().__init__()
        self.name = 'cold_ocean'
        self.display_name = 'Cold Ocean'