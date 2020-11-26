import os
import pathlib
import shutil
from jinja2 import Environment, FileSystemLoader
import json

import config

from jinja2 import Environment, FileSystemLoader

def set_enchantment(block_dict, enchatment):
    if block_dict.get('Items') is None or len(block_dict['Items']) == 0:
        block_dict['Items'] = [{}]

    block_dict['Items'][0]['tag'] = {'Enchantments': [{'id': enchatment}]}
    return block_dict


def workstation_state(item="0+", enchantment=None, force_slot=False):
    workstation_settings = config.datapack_settings['workstation']
    mcitem = 'minecraft:stone'
    block_dict = {
        'id': workstation_settings['item'],
        'CustomName': "{'text':'" + workstation_settings['name'] + "'}"
    }

    if item == '0':
        block_dict['Items'] = []
    elif item == '1+':
        block_dict['Items'] = [{}]
    elif item == 'tool_slot':
        block_dict['Items'] = [{'Slot': workstation_settings['slot'] }]
    elif item.find('minecraft:') >= 0:
        block_dict['Items'] = [{'id': item, 'Slot': workstation_settings['slot'] }]

    if enchantment:
        block_dict = set_enchantment(block_dict, enchantment)

    block_dict_str = json.dumps(block_dict)
    block_dict_str = block_dict_str.replace('\\"', "'")
    block_dict_str = block_dict_str.replace("\"{'text':", '\'{"text":')
    block_dict_str = block_dict_str.replace("'" + workstation_settings['name'] + "'}\"", '"' + workstation_settings['name'] + '"}\'')
    block_dict_str = block_dict_str.replace(f'"Slot": {workstation_settings["slot"]}', f'"Slot": {workstation_settings["slot"]}b')
    
    conditonal = f'data block {workstation_settings["coords"]} {block_dict_str}'
    return conditonal

def workstation_conditional(tool, opt_key, options, usage="items"):
    condition = ''
    opt_gives = options[opt_key]

    if opt_gives.get(usage) is None:
        return condition

    ifs = []
    unlesses = []

    if opt_key == 'default':
        ifs.append(workstation_state(item=tool))
    elif opt_gives['type'] == 'enchantment':
        if tool == '0+':
            tool = 'tool_slot'
        ifs.append(workstation_state(item=tool, enchantment=opt_key))

    all_curr_opt_keys = opt_gives.keys()
    for opt in options:
        if opt == 'default' or opt == opt_key:
            continue

        overrides_usage = usage in opt_gives and usage in options[opt]

        if not overrides_usage:
            continue

        if options[opt]['type'] == 'item':
            unlesses.append(workstation_state(item=opt))
        elif options[opt]['type'] == 'enchantment':
            unlesses.append(workstation_state(item='tool_slot', enchantment=opt))

    ifs_str = ' if '.join(ifs)
    unlesses_str = ' unless '.join(unlesses)
    if len(ifs_str) > 0:
        condition = f'if {ifs_str}'

    if len(unlesses_str) > 0:
        condition = f'{condition} unless {unlesses_str}'

    return condition

def region_gives(opt_key, options):
    extended_options = dict(options["default"], **options[opt_key])
    return extended_options
        

env = Environment(loader=FileSystemLoader('/path/to/templates'))

env = Environment(
    variable_start_string='<<',
    variable_end_string='>>',
    comment_start_string='/*',
    comment_end_string='*/',
    autoescape=False,
    trim_blocks=True,
    lstrip_blocks=True,
    loader=FileSystemLoader(config.SOURCE_DIR),
)
env.globals['workstation_state'] = workstation_state
env.globals['workstation_conditional'] = workstation_conditional
env.globals['region_gives'] = region_gives

if os.path.isdir(config.DIST_DIR):
    shutil.rmtree(config.DIST_DIR)

pathlib.Path(config.DIST_DIR).mkdir(parents=True, exist_ok=True)

for (dirpath, dirnames, filenames) in os.walk(config.SOURCE_DIR):
    if dirpath == config.TEMPLATES_DIR:
        continue
    
    output_dir = dirpath.replace(config.SOURCE_DIR, config.DIST_DIR)
    pathlib.Path(output_dir).mkdir(parents=True, exist_ok=True)

    for f in filenames:
        template_path = os.path.join(dirpath, f)
        template_path = template_path.replace(f"{config.SOURCE_DIR}/", '')
        template = env.get_template(template_path)
        
        output_file = f.replace('.j2', '')
        output_path = os.path.join(output_dir, output_file)
        output = template.render(**config.datapack_settings)

        with open(output_path, "w") as fh:
            fh.write(output)