from .jungle import Jungle

class ModifiedJungle(Jungle):
    def __init__(self):
        super().__init__()
        self.name = 'modified_jungle'
        self.display_name = 'Modified Jungle'
        