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
        "workstation": "cc_workstation",
    },
    "activation": {
        "item": "minecraft:stone_button",
        "radius": 4,
    },
    "workstation": {
        "item": "minecraft:barrel",
        "name": "Chillcraft Workstation",
        "lore": "Gathers biome resources with magic",
        "give_items": [{"Slot":0, "id":"minecraft:stone_button", "Count":1}],
        "coords": "~ ~-1 ~",
        "slot": 0,
    },
    "supported_tools": {
        "axes": ["minecraft:wooden_axe", "minecraft:stone_axe", "minecraft:iron_axe", "minecraft:gold_axe", "minecraft:diamond_axe", "minecraft:netherite_axe"],
        "pickaxes": ["minecraft:wooden_pickaxe", "minecraft:stone_pickaxe", "minecraft:iron_pickaxe", "minecraft:gold_pickaxe", "minecraft:diamond_pickaxe", "minecraft:netherite_pickaxe"]
    },
    "biomes": {},
}

datapack_settings['wait_ticks'] = datapack_settings.get('ticks_per_second', 20) * datapack_settings.get('wait_seconds', 0)


datapack_settings["biomes"]["forest"] = {
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
datapack_settings["biomes"]["forest"]["supported_tools"] = [tool for tool in datapack_settings["biomes"]["forest"]["resources"].keys() if tool != "0+"]