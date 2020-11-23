execute if score @p elapsed_time < WAIT_TICKS WAIT_TICKS run scoreboard players add @p elapsed_time 1

execute as @p at @p if block ~1 ~ ~ minecraft:stone_button[powered=true] run function chillcraft:grind_biome
execute as @p at @p if block ~-1 ~ ~ minecraft:stone_button[powered=true] run function chillcraft:grind_biome
execute as @p at @p if block ~ ~1 ~ minecraft:stone_button[powered=true] run function chillcraft:grind_biome
execute as @p at @p if block ~ ~-1 ~ minecraft:stone_button[powered=true] run function chillcraft:grind_biome
execute as @p at @p if block ~ ~ ~1 minecraft:stone_button[powered=true] run function chillcraft:grind_biome
execute as @p at @p if block ~ ~ ~-1 minecraft:stone_button[powered=true] run function chillcraft:grind_biome