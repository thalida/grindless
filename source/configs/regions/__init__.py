from .forest import Forest
from .dark_forest import DarkForest
from .badlands import Badlands
from .badlands_plateau import BadlandsPlateau

region_classes = {
    'forest': Forest,
    'dark_forest': DarkForest,
    'badlands': Badlands,
    'badlands_plateau': BadlandsPlateau
}