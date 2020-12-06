"""
Overworld Mines
===========================================================

Submodules
----------

grindless.settings.regions.overworld\_mines.diamond\_mine module
-------------------------------------------------------------------------

.. automodule:: grindless.settings.regions.overworld_mines.diamond_mine
   :members:
   :undoc-members:
   :show-inheritance:

grindless.settings.regions.overworld\_mines.surface\_mine module
-------------------------------------------------------------------------

.. automodule:: grindless.settings.regions.overworld_mines.surface_mine
   :members:
   :undoc-members:
   :show-inheritance:
"""

import os
import importlib

for module in os.listdir(os.path.join(os.path.dirname(__file__))):
    if module == '__init__.py' or module == 'base_region.py' or module[-3:] != '.py':
        continue

    __import__(module[:-3], locals(), globals(), [], 1)

del os
del importlib
del module