import os
import json
import copy

VERSION = 1

DIR_PATH = os.path.dirname(os.path.realpath(__file__))
SOURCE_DIR = os.path.realpath('./source')
DIST_FOLDER = './dist'
DIST_DIR = os.path.realpath(DIST_FOLDER)
TEMPLATES_DIR = os.path.join(SOURCE_DIR, 'templates')

datapack_settings = {
    "ticks_per_second": 20,
    "wait_seconds": 10,
    "scoreboards": {
        "gathering": "cc_gathering",
        "item_damage": "cc_item_damage",
        "elapsed_time": "cc_elapsed_time",
    },
    "activation": {
        "item": "minecraft:stone_button",
        "radius": 4,
    },
    "workbench": {
        "item": "minecraft:barrel",
        "name": "Chillcraft Workbench",
        "coords": "~ ~-1 ~",
        "slot": 0,
    },
    "supported_tools": {
        "axes": ["minecraft:wooden_axe", "minecraft:stone_axe", "minecraft:iron_axe", "minecraft:gold_axe", "minecraft:diamond_axe", "minecraft:netherite_axe"],
        "pickaxes": ["minecraft:wooden_pickaxe", "minecraft:stone_pickaxe", "minecraft:iron_pickaxe", "minecraft:gold_pickaxe", "minecraft:diamond_pickaxe", "minecraft:netherite_pickaxe"]
    },
    "gives": None
}

datapack_settings['wait_ticks'] = datapack_settings.get('ticks_per_second', 20) * datapack_settings.get('wait_seconds', 0)

datapack_settings["gives"] = {
    "forest": {
        "no_tool": {
            "items": {
                "minecraft:oak_log": 8,
                "minecraft:birch_log": 8,
            },
            "damage": 0
        },
        "any_tool": {
            "items": {
                "minecraft:oak_log": 8,
                "minecraft:birch_log": 8,
            },
            "damage": 0
        },
        "minecraft:wooden_axe": {
            "items": {
                "minecraft:oak_log": 8,
                "minecraft:birch_log": 8,
            },
            "damage": 4
        },
        "minecraft:stone_axe": {
            "items": {
                "minecraft:oak_log": 12,
                "minecraft:birch_log": 12,
            },
            "damage": 5
        },
        "minecraft:iron_axe": {
            "items": {
                "minecraft:oak_log": 24,
                "minecraft:birch_log": 24,
            },
            "damage": 8
        },
        "minecraft:diamond_axe": {
            "items": {
                "minecraft:oak_log": 28,
                "minecraft:birch_log": 28,
            },
            "damage": 9
        },
        "minecraft:netherite_axe": {
            "items": {
                "minecraft:oak_log": 32,
                "minecraft:birch_log": 32,
            },
            "damage": 10
        },
        "minecraft:gold_axe": {
            "items": {
                "minecraft:oak_log": 40,
                "minecraft:birch_log": 40,
            },
            "damage": 12
        },
    }
}
