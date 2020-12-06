"""
End
==============================================

grindless.settings.regions.end.end\_barrens module
----------------------------------------------------------

.. automodule:: grindless.settings.regions.end.end_barrens
   :members:
   :undoc-members:
   :show-inheritance:

grindless.settings.regions.end.end\_highlands module
------------------------------------------------------------

.. automodule:: grindless.settings.regions.end.end_highlands
   :members:
   :undoc-members: 
   :show-inheritance:

grindless.settings.regions.end.end\_midlands module
-----------------------------------------------------------

.. automodule:: grindless.settings.regions.end.end_midlands
   :members:
   :undoc-members:
   :show-inheritance:

grindless.settings.regions.end.small\_end\_islands module
-----------------------------------------------------------------

.. automodule:: grindless.settings.regions.end.small_end_islands
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