from .forest import Forest

class WoodedHills(Forest):
    def __init__(self):
        super().__init__()
        self.name = 'wooded_hills'
        self.display_name = 'Wooded Hills'
        