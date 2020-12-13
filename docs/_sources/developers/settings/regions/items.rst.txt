.. _settings-regions-items:

Items
==================

``items.yaml`` includes every supported item in the datapack.

Each item defines what tools are supported, and provides a multiplier
from 0 to 1 of how much the tool provides. ``1`` is the default item multiplier

The item multiplier is used in conjunction with the region,
:ref:`tool<settings-tools>`, and :ref:`enchantment<settings-enchantments>`
multipliers to calculate exactly how much of an item should be given.

`View items.yaml on Github <https://github.com/thalida/grindless/tree/main/grindless/settings/regions/items.yaml>`_

----

Sample Item Definitions
-------------------------

Simple
^^^^^^^
The following code defines ``basalt``:

* as only given by a pickaxe
* and by default gives 100% (1) of what the region and pickaxe normally would produce

.. code-block:: yaml

  minecraft:basalt:
    pickaxe:
      default: 1

Any Tool
^^^^^^^^^^^
``any`` is a unique in that it is a fallback that's captured if any tool is put into the
tool slot of the workstation.

The following code defines ``apple``:

* as an item given by any tool or an axe
* and by default gives 100% (1) of what the region and axe normally would produce

.. code-block:: yaml

    minecraft:apple:
      any:
        default: 1
      axe:
        default: 1

Specific Material and Tool
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Some items require a specific material and tool type combination in order to be
given.

The following code defines ``diamond``:

* as an item given by only iron, diamond, gold, and netherite pickaxes
* and by default gives 100% (1) of what the region and pickaxe normally would produce

.. code-block:: yaml

    minecraft:diamond:
      iron_pickaxe:
        default: 1
      diamond_pickaxe:
        default: 1
      golden_pickaxe:
        default: 1
      netherite_pickaxe:
        default: 1

Silk Touch
^^^^^^^^^^^
Some items require the silk touch enchantment in order to be mined, while others
may give a reduced quantity of items when mined with silk touch.

The following code defines ``gravel``:

* as an item given by any tool or a shovel
* by default the amount of gravel produced is 20% of what would normally be given
* if the tool has silk touch then the amount of gravel is produced 80% of what would be given

The following code defines ``flint``:

* as an item given by any tool or a shovel
* by default the amount of flint produced is 80% of what would normally be given
* if the tool has silk touch then the amount of flint is produced 20% of what would be given

.. code-block:: yaml

    minecraft:gravel:
      any:
        default: 0.2
        minecraft:silk_touch: 0.8
      shovel:
        default: 0.2
        minecraft:silk_touch: 0.8

    minecraft:flint:
      any:
        default: 0.8
        minecraft:silk_touch: 0.2
      shovel:
        default: 0.8
        minecraft:silk_touch: 0.2

With both of these item definitions, if the tool in the workbench is a shovel...

* and it **does not** have silk touch: then the player will be given 20% gravel and 80% flint
* and it **does** have silk touch: then the player will be given 20% flint and 80% gravel

In the following example, ``melon`` is defined as:

* as an item given by any tool or an axe
* by default it gives 100% of would normally be produced
* if the tool has silk touch then zero melon slices will be given

.. code-block:: yaml

    minecraft:melon_slice:
      any:
        default: 1
        minecraft:silk_touch: 0
      axe:
        default: 1
        minecraft:silk_touch: 0


Using Extends
^^^^^^^^^^^^^^^
There are many items whose definitions share common characteristics.
The ``items`` yaml file uses the extends feature built into yaml to reduce duplications.

The code snippet below defines all of the oak variants as extensions of the default
leaves, logs, and sappling item definitions.

.. code-block:: yaml

    minecraft:oak_leaves:
      <<: *leaves
    minecraft:oak_log:
      <<: *logs
    minecraft:oak_sapling:
      <<: *sappling

----

Supported Extends
------------------

There are only a handful of groups currently defined for quick extending:

* Leaves
* Logs
* Sappling
* Flowers
* Coral
* Coral Block
* Coral Fan
* Mushroom
* Mushroom Block
* Sand
* Terracotta
