"""
Regions
==================================

.. autosummary::
   grindless.settings
   grindless.settings.regions
   grindless.settings.regions.base_region
   grindless.settings.regions.end
   grindless.settings.regions.end.end_barrens

----

.. toctree::
   :maxdepth: 1

   items
   base_region


Supported Regions
------------------------
.. toctree::
   :maxdepth: 1

   end/index
   nether/index
   overworld/index
   overworld_mines/index

"""

from .overworld import *
from .overworld_mines import *
from .nether import *
from .end import *

del overworld
del overworld_mines
del nether
del end