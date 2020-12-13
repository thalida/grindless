.. _settings-gather:

Gather
==================

``gather.yaml`` houses the settings for how and when you can quickly gather materials for a region.

.. rubric:: Settings
.. list-table::
    :widths: 25 100
    :header-rows: 1

    * - Variable
      - Description

    * - ``wait_seconds``
      - The number of seconds between each activation.

        This number is converted to ticks.

    * - ``activation_radius``
      - How close to the ``activation_item`` do we need to be?

        This number represents N blocks in all directions (x, y, z)

    * - ``activation_item``
      - What game item do we power to activate gathering the items for a region?

    * - ``workstation``
      - A dict defining the settings for a workstation. See list of supported keys below.

.. rubric:: Workstation Settings
.. list-table::
    :header-rows: 1
    :widths: 25 100

    * - Workstation Key
      - Value

    * - ``item``
      - Must be a Minecraft storage block

    * - ``name``
      - Custom name for the workstation item.

    * - ``lore``
      - The lore that should be displayed when hovered over the item.

    * - ``coords``
      - Where should the workstation be relative to the player?

        ``~ ~-1 ~`` means the player should be standing on the item.

        X equals the player's current X coord.

        Y equals 1 block _below_ the player.

        Z equals the player's current Z coord.

    * - ``slot``
      - In which storage slot should we look for the chosen tool?


    * - ``give_items``
      - What other items should be given with a workstation?

        This is used by the `kit` trigger :doc:`../datapacks/grindless/functions/index`

----

.. rubric:: Source: (`View file on Github <https://github.com/thalida/grindless/tree/main/grindless/settings/gather.yaml>`_)

.. literalinclude:: /../grindless/settings/gather.yaml
   :language: yaml
