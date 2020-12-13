.. _settings-tools:

Tools
==================

``tools.yaml`` defines the supported tools, materials, and the multipliers for giving items and damage.

.. rubric:: Settings
.. list-table::
    :widths: 25 100
    :header-rows: 1

    * - Variable
      - Description

    * - ``supported_tools``
      - List of all tools supported by the datapack

    * - ``supported_materials``
      - List of all supported materials.

        This is a list of prefixes not names, eg. ``golden`` instead of ``gold``.

    * - ``tools_without_material``
      - List of all tools that don't take a material (eg. shears)

    * - ``item_multipliers_by_material``
      - Defines how much of an item should be given per material

        For example, ``diamond`` should give more items than ``wooden`` tools.

    * - ``damage_multipliers_by_material``
      - Defines how much of damage should be given per material.

        This should include any number between 0 and 1.

        A damage of ``1`` would mean if you are given 100 items the tool would take 100 damage.

        A damage of ``0.5`` would mean if you are given 100 items the tool would take 50 damage.

----

.. rubric:: Source: (`View file on Github <https://github.com/thalida/grindless/tree/main/grindless/settings/tools.yaml>`_)

.. literalinclude:: /../grindless/settings/tools.yaml
   :language: yaml
