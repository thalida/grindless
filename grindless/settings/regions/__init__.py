"""
.. _settings-regions:

Regions
==================================

The region settings define what items are given by a region.

Items
   A master list of all items supported by the datapack.
   This list is used to generate the region configs.

   Learn more about :ref:`Items <settings-regions-items>`.

BaseRegion
   The base class for all regions.
   Contains the logic to generate the region settings dict.

   Learn more about :ref:`BaseRegion <settings-regions-baseregion>`.

.. toctree::
   :maxdepth: 1
   :hidden:

   items
   base_region


Supported Dimensions
------------------------
Explore the dimensions below to learn more about the supported regions / biomes.

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
