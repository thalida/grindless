"""
Nether
=================================================

Submodules
----------

grindless.settings.regions.nether.basalt\_deltas module
---------------------------------------------------------------

.. automodule:: grindless.settings.regions.nether.basalt_deltas
   :members:
   :undoc-members:
   :show-inheritance:

grindless.settings.regions.nether.crimson\_forest module
----------------------------------------------------------------

.. automodule:: grindless.settings.regions.nether.crimson_forest
   :members:
   :undoc-members:
   :show-inheritance:

grindless.settings.regions.nether.nether\_wastes module
----------------------------------------------------------------

.. automodule:: grindless.settings.regions.nether.nether_wastes
   :members:
   :undoc-members:
   :show-inheritance:

grindless.settings.regions.nether.soul\_sand\_valley module
-------------------------------------------------------------------

.. automodule:: grindless.settings.regions.nether.soul_sand_valley
   :members:
   :undoc-members:
   :show-inheritance:

grindless.settings.regions.nether.warped\_forest module
---------------------------------------------------------------

.. automodule:: grindless.settings.regions.nether.warped_forest
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