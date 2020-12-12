Scoreboards
==================

``scoreboards.yaml`` defines all of the keys for the scoreboards used by the datapack.

.. rubric:: Settings
.. list-table::
    :widths: 25 100
    :header-rows: 1

    * - Scoreboard Key
      - Scoreboard Name
   
    * - ``gathering``
      - Used to track if the player is gathering or not.
        
        Mimics a boolean where 1 is ``true`` and 0 is ``false``.
   
    * - ``item_damage``
      - Stores how much damage the item (tool) used during gathering has
   
    * - ``elapsed_time``
      - Tracks how much time has elapsed since the last gather. 
      
        Maxes out at the ``wait_seconds`` defined in the Gather settings.
   
    * - ``yaxis``
      - Stores the players ``y-axis`` at the time of gathering.
      
        Used when determining what region a player is in.

    * - ``help``
      - Tracks if the player has triggered the help command. See functions/triggers/help.

    * - ``kit``
      - Tracks if the player has triggered the kit command. See functions/triggers/kit.

.. rubric:: Entire File:

`View on Github <https://github.com/thalida/grindless/tree/staging/grindless/settings/scoreboards.yaml>`_

.. literalinclude:: /../grindless/settings/scoreboards.yaml
   :language: yaml