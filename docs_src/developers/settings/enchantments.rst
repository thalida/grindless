.. _settings-enchantments:

Enchantments
==================

``enchantments.yaml`` defines which enchantments are supported,
and how they effect the amount of items and damage given.

.. rubric:: Settings
.. list-table::
    :widths: 25 100
    :header-rows: 1

    * - Variable
      - Description

    * - ``enabled``
      - Are enchantments enabled on the datapack?

        If ``false`` enchantments will not affect the items or damage given.

    * - ``supported_enchantments``
      - List of which enchantments are supported by the datapack

    * - ``supported_enchantments_by_tool``
      - List of enchantments supported for each tool.

        (Not all tools support the same enchantments in Minecraft.)

    * - ``item_multipliers_by_enchantment``
      - Defines how much more of an item should be given if the tool has the enchantment.

        For example, a tool with ``efficiency`` will gives 1.2x more items.

    * - ``damage_multipliers_by_enchantment``
      - Defines how much damage a tool will receive

        For example, a tool with ``unbreaking`` will get 50% less damage

----

.. rubric:: Source: (`View file on Github <https://github.com/thalida/grindless/tree/main/grindless/settings/enchantments.yaml>`_)

.. literalinclude:: /../grindless/settings/enchantments.yaml
   :language: yaml
