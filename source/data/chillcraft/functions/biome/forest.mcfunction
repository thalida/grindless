scoreboard players set is_grinding is_grinding 1

# ===========
# Show Title & subtitle
# ---------------------------------------------------------------------------
title @s times 5 100 5
execute if data block ~ ~-1 ~ {Items: []} run title @s title { "text":"Gathering", "bold":true }
execute if data block ~ ~-1 ~ {Items:[{}]} run title @s title { "text":"Gathering", "bold":true }

execute if data block ~ ~-1 ~ {Items: []} run title @s subtitle { "text":"In a forest with no tools", "italic": true }
execute if data block ~ ~-1 ~ Items[{id: "minecraft:wooden_axe", Slot: 0b}] run title @s subtitle { "text":"In a forest with a wooden axe", "italic":true }
execute if data block ~ ~-1 ~ Items[{id: "minecraft:stone_axe", Slot: 0b}] run title @s subtitle { "text":"In a forest with a stone axe", "italic":true }
execute if data block ~ ~-1 ~ Items[{id: "minecraft:iron_axe", Slot: 0b}] run title @s subtitle { "text":"In a forest with a iron axe", "italic":true }
execute if data block ~ ~-1 ~ Items[{id: "minecraft:diamond_axe", Slot: 0b}] run title @s subtitle { "text":"In a forest with a diamond axe", "italic":true }
execute if data block ~ ~-1 ~ Items[{id: "minecraft:netherite_axe", Slot: 0b}] run title @s subtitle { "text":"In a forest with a netherite axe", "italic":true }
execute if data block ~ ~-1 ~ Items[{id: "minecraft:golden_axe", Slot: 0b}] run title @s subtitle { "text":"In a forest with a golden axe", "italic":true }
execute unless data block ~ ~-1 ~ {Items: []} unless data block ~ ~-1 ~ Items[{id: "minecraft:wooden_axe", Slot: 0b}] unless data block ~ ~-1 ~ Items[{id: "minecraft:stone_axe", Slot: 0b}] unless data block ~ ~-1 ~ Items[{id: "minecraft:iron_axe", Slot: 0b}] unless data block ~ ~-1 ~ Items[{id: "minecraft:diamond_axe", Slot: 0b}] unless data block ~ ~-1 ~ Items[{id: "minecraft:netherite_axe", Slot: 0b}] unless data block ~ ~-1 ~ Items[{id: "minecraft:golden_axe", Slot: 0b}] run title @s subtitle { "text":"In a forest without an appropriate tool", "italic":true }

# ===========
# Save Damage
# ---------------------------------------------------------------------------
scoreboard players set item_damage item_damage 0
execute if data block ~ ~-1 ~ {Items:[{}]} store result score item_damage item_damage run data get block ~ ~-1 ~ Items[0].tag.Damage 1

# ===========
# Do Work
# ---------------------------------------------------------------------------
#   AXES
# ---------------------------------------------------------------------------
# Breaking Time: 3s / log
execute unless data block ~ ~-1 ~ Items[{id: "minecraft:wooden_axe", Slot: 0b}] unless data block ~ ~-1 ~ Items[{id: "minecraft:stone_axe", Slot: 0b}] unless data block ~ ~-1 ~ Items[{id: "minecraft:iron_axe", Slot: 0b}] unless data block ~ ~-1 ~ Items[{id: "minecraft:diamond_axe", Slot: 0b}] unless data block ~ ~-1 ~ Items[{id: "minecraft:netherite_axe", Slot: 0b}] unless data block ~ ~-1 ~ Items[{id: "minecraft:golden_axe", Slot: 0b}] run give @p oak_log 8
execute unless data block ~ ~-1 ~ Items[{id: "minecraft:wooden_axe", Slot: 0b}] unless data block ~ ~-1 ~ Items[{id: "minecraft:stone_axe", Slot: 0b}] unless data block ~ ~-1 ~ Items[{id: "minecraft:iron_axe", Slot: 0b}] unless data block ~ ~-1 ~ Items[{id: "minecraft:diamond_axe", Slot: 0b}] unless data block ~ ~-1 ~ Items[{id: "minecraft:netherite_axe", Slot: 0b}] unless data block ~ ~-1 ~ Items[{id: "minecraft:golden_axe", Slot: 0b}] run give @p birch_log 8

# Breaking Time: 1.5s / log
execute if data block ~ ~-1 ~ Items[{id: "minecraft:wooden_axe", Slot: 0b}] run give @s oak_log 16
execute if data block ~ ~-1 ~ Items[{id: "minecraft:wooden_axe", Slot: 0b}] run give @s birch_log 16
execute if data block ~ ~-1 ~ Items[{id: "minecraft:wooden_axe", Slot: 0b}] run scoreboard players add item_damage item_damage 4

# Breaking Time: 0.75s / log
execute if data block ~ ~-1 ~ Items[{id: "minecraft:stone_axe", Slot: 0b}] run give @s oak_log 20
execute if data block ~ ~-1 ~ Items[{id: "minecraft:stone_axe", Slot: 0b}] run give @s birch_log 20
execute if data block ~ ~-1 ~ Items[{id: "minecraft:stone_axe", Slot: 0b}] run scoreboard players add item_damage item_damage 5


# Breaking Time: 0.5s / log
execute if data block ~ ~-1 ~ Items[{id: "minecraft:iron_axe", Slot: 0b}] run give @s oak_log 32
execute if data block ~ ~-1 ~ Items[{id: "minecraft:iron_axe", Slot: 0b}] run give @s birch_log 32
execute if data block ~ ~-1 ~ Items[{id: "minecraft:iron_axe", Slot: 0b}] run scoreboard players add item_damage item_damage 8


# Breaking Time: 0.4s / log
execute if data block ~ ~-1 ~ Items[{id: "minecraft:diamond_axe", Slot: 0b}] run give @s oak_log 36
execute if data block ~ ~-1 ~ Items[{id: "minecraft:diamond_axe", Slot: 0b}] run give @s birch_log 36
execute if data block ~ ~-1 ~ Items[{id: "minecraft:diamond_axe", Slot: 0b}] run scoreboard players add item_damage item_damage 9


# Breaking Time: 0.35s / log
execute if data block ~ ~-1 ~ Items[{id: "minecraft:netherite_axe", Slot: 0b}] run give @s oak_log 40
execute if data block ~ ~-1 ~ Items[{id: "minecraft:netherite_axe", Slot: 0b}] run give @s birch_log 40
execute if data block ~ ~-1 ~ Items[{id: "minecraft:netherite_axe", Slot: 0b}] run scoreboard players add item_damage item_damage 10


# Breaking Time: 0.25s / log
execute if data block ~ ~-1 ~ Items[{id: "minecraft:golden_axe", Slot: 0b}] run give @s oak_log 48
execute if data block ~ ~-1 ~ Items[{id: "minecraft:golden_axe", Slot: 0b}] run give @s birch_log 48
execute if data block ~ ~-1 ~ Items[{id: "minecraft:golden_axe", Slot: 0b}] run scoreboard players add item_damage item_damage 12


# ===========
# Update Damage
# ---------------------------------------------------------------------------
execute if data block ~ ~-1 ~ Items[{Slot: 0b}] store result block ~ ~-1 ~ Items[0].tag.Damage int 1 run scoreboard players get item_damage item_damage


# ===========
# Start Wait...
# ---------------------------------------------------------------------------
execute if data block ~ ~-1 ~ {Items: []} run scoreboard players set elapsed_time elapsed_time 0
execute if data block ~ ~-1 ~ {Items:[{}]} run scoreboard players set elapsed_time elapsed_time 0

scoreboard players set is_grinding is_grinding 0
