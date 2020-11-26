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
    "namespace": "grindless",
    "ticks_per_second": 20,
    "wait_seconds": 10,

}

datapack_settings["scoreboards"] = {
    "gathering": "gl_gathering",
    "item_damage": "gl_item_damage",
    "elapsed_time": "gl_elapsed_time",
    "help": "grindless_help",
    "kit": "grindless_kit",
}

datapack_settings["activation"] = {
    "item": "minecraft:warped_button",
    "radius": 4,
}

datapack_settings["workstation"] = {
    "item": "minecraft:barrel",
    "name": "Grindless Workstation",
    "lore": "Gather resources through magic",
    "give_items": [{
        "Slot": 0,
        "id": datapack_settings["activation"]["item"],
        "Count": 1
    }],
    "coords": "~ ~-1 ~",
    "slot": 0,
}

datapack_settings['wait_ticks'] = datapack_settings.get('ticks_per_second', 20) * datapack_settings.get('wait_seconds', 0)

datapack_settings["regions"] = {}
datapack_settings["regions"]["forest"] = {
    "id": "forest",
    "display_name": "Forest",
    "resources": {
        "0+": {
            "default": {
                "items": {
                    "minecraft:oak_log": 8,
                    "minecraft:birch_log": 8,
                    "minecraft:oak_sapling": 4,
                    "minecraft:birch_sapling": 4,
                    "minecraft:stick": 4,
                    "minecraft:apple": 2,
                },
                "damage": 0,
            },
            "minecraft:silk_touch": {
                "type": "enchantment",
                "items": {
                    "minecraft:oak_leaves": 16,
                    "minecraft:birch_leaves": 16,
                }
            },
            "minecraft:shears": {
                "type": "item",
                "items": None,
            }
        },
        "minecraft:wooden_axe": {
            "default": {
                "items": {
                    "minecraft:oak_log": 8,
                    "minecraft:birch_log": 8,
                },
                "damage": 4,
            },
            "minecraft:unbreaking": {
                "type": "enchantment",
                "damage": 2,
            },
            "minecraft:silk_touch": {
                "type": "enchantment",
                "items": {
                    "minecraft:oak_leaves": 16,
                    "minecraft:birch_leaves": 16,
                },
            }
        },
        "minecraft:stone_axe": {
            "default": {
                "items": {
                    "minecraft:oak_log": 12,
                    "minecraft:birch_log": 12,
                },
                "damage": 5
            },
            "minecraft:unbreaking": {
                "type": "enchantment",
                "damage": 2,
            },
            "minecraft:silk_touch": {
                "type": "enchantment",
                "items": {
                    "minecraft:oak_leaves": 24,
                    "minecraft:birch_leaves": 24,
                },
            }
        },
        "minecraft:iron_axe": {
            "default": {
                "items": {
                    "minecraft:oak_log": 24,
                    "minecraft:birch_log": 24,
                },
                "damage": 8
            },
            "minecraft:unbreaking": {
                "type": "enchantment",
                "damage": 4,
            },
            "minecraft:silk_touch": {
                "type": "enchantment",
                "items": {
                    "minecraft:oak_leaves": 48,
                    "minecraft:birch_leaves": 48,
                }
            }
        },
        "minecraft:diamond_axe": {
            "default": {
                "items": {
                    "minecraft:oak_log": 28,
                    "minecraft:birch_log": 28,
                },
                "damage": 9
            },
            "minecraft:unbreaking": {
                "type": "enchantment",
                "damage": 4,
            },
            "minecraft:silk_touch": {
                "type": "enchantment",
                "items": {
                    "minecraft:oak_leaves": 56,
                    "minecraft:birch_leaves": 56,
                },
            }
        },
        "minecraft:netherite_axe": {
            "default": {
                "items": {
                    "minecraft:oak_log": 32,
                    "minecraft:birch_log": 32,
                },
                "damage": 10
            },
            "minecraft:unbreaking": {
                "type": "enchantment",
                "damage": 5,
            },
            "minecraft:silk_touch": {
                "type": "enchantment",
                "items": {
                    "minecraft:oak_leaves": 64,
                    "minecraft:birch_leaves": 64,
                },
            }
        },
        "minecraft:gold_axe": {
            "default": {
                "items": {
                    "minecraft:oak_log": 40,
                    "minecraft:birch_log": 40,
                },
                "damage": 12
            },
            "minecraft:unbreaking": {
                "type": "enchantment",
                "damage": 6,
            },
            "minecraft:silk_touch": {
                "type": "enchantment",
                "items": {
                    "minecraft:oak_leaves": 80,
                    "minecraft:birch_leaves": 80,
                },
            }
        },
        "minecraft:shears": {
            "default": {
                "items": {
                    "minecraft:oak_leaves": 80,
                    "minecraft:birch_leaves": 80,
                },
                "damage": 10
            },
            "minecraft:unbreaking": {
                "type": "enchantment",
                "damage": 5,
            }
        },
    },
    "supported_tools": None,
}
datapack_settings["regions"]["forest"]["supported_tools"] = [tool for tool in datapack_settings["regions"]["forest"]["resources"].keys() if tool != "0+"]