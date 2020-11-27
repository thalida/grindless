import json
import helpers

datapack_configs = helpers.get_datapack_configs()

def set_enchantment(block_dict, enchatment):
    if block_dict.get('Items') is None or len(block_dict['Items']) == 0:
        block_dict['Items'] = [{}]

    block_dict['Items'][0]['tag'] = {'Enchantments': [{'id': enchatment}]}
    return block_dict


def workstation_state(item="0+", enchantment=None, force_slot=False):
    workstation_configs = datapack_configs['gather']['workstation']
    mcitem = 'minecraft:stone'
    block_dict = {
        'id': workstation_configs['item'],
        'CustomName': "{'text':'" + workstation_configs['name'] + "'}"
    }

    if item == '0':
        block_dict['Items'] = []
    elif item == '1+':
        block_dict['Items'] = [{}]
    elif item == 'tool_slot':
        block_dict['Items'] = [{'Slot': workstation_configs['slot'] }]
    elif item.find('minecraft:') >= 0:
        block_dict['Items'] = [{'id': item, 'Slot': workstation_configs['slot'] }]

    if enchantment:
        block_dict = set_enchantment(block_dict, enchantment)

    block_dict_str = json.dumps(block_dict)
    block_dict_str = block_dict_str.replace('\\"', "'")
    block_dict_str = block_dict_str.replace("\"{'text':", '\'{"text":')
    block_dict_str = block_dict_str.replace("'" + workstation_configs['name'] + "'}\"", '"' + workstation_configs['name'] + '"}\'')
    block_dict_str = block_dict_str.replace(f'"Slot": {workstation_configs["slot"]}', f'"Slot": {workstation_configs["slot"]}b')
    
    conditonal = f'data block {workstation_configs["coords"]} {block_dict_str}'
    return conditonal

def workstation_conditional(tool, opt_key, options, region=None, usage="items"):
    condition = ''
    opt_gives = options[opt_key]

    if opt_gives.get(usage) is None:
        return condition

    ifs = []
    unlesses = []

    if opt_key == 'default':
        ifs.append(workstation_state(item=tool))
    else:
        if tool == '0+':
            enchanted_item = 'tool_slot'
        else:
            enchanted_item = tool

        ifs.append(workstation_state(item=enchanted_item, enchantment=opt_key))

    for opt in options:
        if opt == 'default' or opt == opt_key:
            continue

        overrides_usage = usage in opt_gives and usage in options[opt]

        if not overrides_usage:
            continue
        
        unlesses.append(workstation_state(item='tool_slot', enchantment=opt))

    if region is not None and tool == '0+':
        for supported_tool in region["supported_tools"]:
            unlesses.append(workstation_state(item=supported_tool))


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