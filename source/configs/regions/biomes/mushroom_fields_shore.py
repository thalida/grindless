from .mushroom_fields import MushroomFields

class MushroomFieldsShore(MushroomFields):
    def __init__(self):
        super().__init__()
        self.name = 'mushroom_fields_shore'
        self.display_name = 'Mushroom Fields'
        