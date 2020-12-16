from .mushroom_fields import MushroomFields

class MushroomFieldsShore(MushroomFields):
    def setup_region(self):
        super().setup_region()
        self.name = 'mushroom_fields_shore'
        self.display_name = 'Mushroom Fields'
