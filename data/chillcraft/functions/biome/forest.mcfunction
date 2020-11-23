title @a title { "text":"Gathering Resources", "bold":true }
title @a subtitle { "text":"Forest Biome", "color":"dark_green", "italic":true }

# ===========
# Save Damage
# ---------------------------------------------------------------------------
scoreboard players set @p item_damage 0
execute store result score @p item_damage run data get block ~ ~-1 ~ Items[0].tag.Damage 1

# ===========
# Do Work
# ---------------------------------------------------------------------------
#   AXES
# ---------------------------------------------------------------------------
# Breaking Time: 3s / log
execute unless data block ~ ~-1 ~ Items[{id: "minecraft:wooden_axe", Slot: 0b}] unless data block ~ ~-1 ~ Items[{id: "minecraft:stone_axe", Slot: 0b}] unless data block ~ ~-1 ~ Items[{id: "minecraft:iron_axe", Slot: 0b}] unless data block ~ ~-1 ~ Items[{id: "minecraft:diamond_axe", Slot: 0b}] unless data block ~ ~-1 ~ Items[{id: "minecraft:netherite_axe", Slot: 0b}] unless data block ~ ~-1 ~ Items[{id: "minecraft:golden_axe", Slot: 0b}] run give @p oak_log 8
execute unless data block ~ ~-1 ~ Items[{id: "minecraft:wooden_axe", Slot: 0b}] unless data block ~ ~-1 ~ Items[{id: "minecraft:stone_axe", Slot: 0b}] unless data block ~ ~-1 ~ Items[{id: "minecraft:iron_axe", Slot: 0b}] unless data block ~ ~-1 ~ Items[{id: "minecraft:diamond_axe", Slot: 0b}] unless data block ~ ~-1 ~ Items[{id: "minecraft:netherite_axe", Slot: 0b}] unless data block ~ ~-1 ~ Items[{id: "minecraft:golden_axe", Slot: 0b}] run give @p birch_log 8

# Breaking Time: 1.5s / log
execute if data block ~ ~-1 ~ Items[{id: "minecraft:wooden_axe", Slot: 0b}] run give @p oak_log 16
execute if data block ~ ~-1 ~ Items[{id: "minecraft:wooden_axe", Slot: 0b}] run give @p birch_log 16
execute if data block ~ ~-1 ~ Items[{id: "minecraft:wooden_axe", Slot: 0b}] run scoreboard players add @p item_damage 4

# Breaking Time: 0.75s / log
execute if data block ~ ~-1 ~ Items[{id: "minecraft:stone_axe", Slot: 0b}] run give @p oak_log 20
execute if data block ~ ~-1 ~ Items[{id: "minecraft:stone_axe", Slot: 0b}] run give @p birch_log 20
execute if data block ~ ~-1 ~ Items[{id: "minecraft:stone_axe", Slot: 0b}] run scoreboard players add @p item_damage 5


# Breaking Time: 0.5s / log
execute if data block ~ ~-1 ~ Items[{id: "minecraft:iron_axe", Slot: 0b}] run give @p oak_log 32
execute if data block ~ ~-1 ~ Items[{id: "minecraft:iron_axe", Slot: 0b}] run give @p birch_log 32
execute if data block ~ ~-1 ~ Items[{id: "minecraft:iron_axe", Slot: 0b}] run scoreboard players add @p item_damage 8


# Breaking Time: 0.4s / log
execute if data block ~ ~-1 ~ Items[{id: "minecraft:diamond_axe", Slot: 0b}] run give @p oak_log 36
execute if data block ~ ~-1 ~ Items[{id: "minecraft:diamond_axe", Slot: 0b}] run give @p birch_log 36
execute if data block ~ ~-1 ~ Items[{id: "minecraft:diamond_axe", Slot: 0b}] run scoreboard players add @p item_damage 9


# Breaking Time: 0.35s / log
execute if data block ~ ~-1 ~ Items[{id: "minecraft:netherite_axe", Slot: 0b}] run give @p oak_log 40
execute if data block ~ ~-1 ~ Items[{id: "minecraft:netherite_axe", Slot: 0b}] run give @p birch_log 40
execute if data block ~ ~-1 ~ Items[{id: "minecraft:netherite_axe", Slot: 0b}] run scoreboard players add @p item_damage 10


# Breaking Time: 0.25s / log
execute if data block ~ ~-1 ~ Items[{id: "minecraft:golden_axe", Slot: 0b}] run give @p oak_log 48
execute if data block ~ ~-1 ~ Items[{id: "minecraft:golden_axe", Slot: 0b}] run give @p birch_log 48
execute if data block ~ ~-1 ~ Items[{id: "minecraft:golden_axe", Slot: 0b}] run scoreboard players add @p item_damage 12


# ===========
# Update Damage
# ---------------------------------------------------------------------------
execute store result block ~ ~-1 ~ Items[0].tag.Damage int 1 run scoreboard players get @p item_damage


# ===========
# Start Wait...
# ---------------------------------------------------------------------------
scoreboard players operation @p elapsed_time = START_TIME START_TIME



# ===========
# Code Archives
# ---------------------------------------------------------------------------
# execute if data block ~ ~-1 ~ Items[{id: "minecraft:wooden_axe", Slot: 0b}] store result score @p item_damage run data get block ~ ~-1 ~ Items[0].tag.Damage 1
# execute if data block ~ ~-1 ~ Items[{id: "minecraft:wooden_axe", Slot: 0b}] run scoreboard players add @p item_damage 8
# execute store result block ~ ~-1 ~ Items[{id: "minecraft:wooden_axe", Slot: 0b}].tag.Damage int 1 run scoreboard players get @p item_damage


# execute store result score @p item_damage run data get entity @p SelectedItem.tag.Damage 1
# scoreboard players add @p item_damage 10
# execute as @a store result entity @p SelectedItem.tag.Damage int 1 run scoreboard players get @p item_damage
# /data get block ~ ~-1 ~ Items[0].tag.Damage


# execute if data block ~ ~-1 ~ Items[{id: "minecraft:wooden_axe", Slot: 0b}] run data modify block ~ ~-1 ~ Items[0] merge value {tag: {Damage: 8}}


# data modify block ~2 ~ ~ Items[0] merge value {tag: {Damage: 30}}

# silk touch
# Grass Block
# everything else
# Dirt
# Oak Log
# Oak Leaves
# Birch Log
# Birch Leaves
# @e[limit=1,type=item,nbt={Item:{tag:{display:{Name:"{'text':'demo'}"}}, Slot: 0b}]
