title @a title { "text":"Gathering Resources", "bold":true }
title @a subtitle { "text":"Forest Biome", "color":"dark_green", "italic":true }

execute if entity @p[nbt={SelectedItem:{id:"minecraft:diamond_sword"}]

# shovel
	# silk touch
		# Grass Block

	# everything else
		# Dirt

# Oak Log
# Oak Leaves
# Birch Log
# Birch Leaves

scoreboard players set @p Grind_Timer 0 

