import json
import grindless.helpers as helpers

def set_enchantments(block_dict, enchatments):
    if block_dict.get('Items') is None or len(block_dict['Items']) == 0:
        block_dict['Items'] = [{}]

    formatted_enchantments = []
    for enchantment in enchatments:
        formatted_enchantments.append({'id': enchantment})
    
    block_dict['Items'][0]['tag'] = {'Enchantments': formatted_enchantments}

    return block_dict


def region_unlesses(region_type):
    datapack_configs = helpers.get_datapack_configs()

    unlesses = []
    for region in datapack_configs[region_type]:
        unless_region = f"unless predicate {datapack_configs['datapack']['namespace']}:{region}"
        unlesses.append(unless_region)

    return ' '.join(unlesses)


def workstation_state(item="0+", enchantments=[], decorated=True):
    datapack_configs = helpers.get_datapack_configs()
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

    
    if not isinstance(enchantments, list):
        enchantments = [enchantments]

    if len(enchantments) > 0:
        block_dict = set_enchantments(block_dict, enchantments)

    if not decorated:
       del block_dict['id']
       del block_dict['CustomName']

    block_dict_str = json.dumps(block_dict)
    block_dict_str = block_dict_str.replace('\\"', "'")
    block_dict_str = block_dict_str.replace("\"{'text':", '\'{"text":')
    block_dict_str = block_dict_str.replace("'" + workstation_configs['name'] + "'}\"", '"' + workstation_configs['name'] + '"}\'')
    block_dict_str = block_dict_str.replace(f'"Slot": {workstation_configs["slot"]}', f'"Slot": {workstation_configs["slot"]}b')

    conditonal = f'data block {workstation_configs["coords"]} {block_dict_str}'
    return conditonal


def workstation_conditional(tool, subtype, tool_stanza, region=None):
    condition = ''
    subtype_stanza = tool_stanza[subtype]

    ifs = []
    unlesses = []

    subtype_parts = subtype.split('/')
    primary_subtype = subtype_parts[0]
    
    enchantments = []
    if primary_subtype != 'default':
        enchantments.append(primary_subtype)
    
    if len(subtype_parts) > 1:
        enchantments = enchantments + subtype_parts[1].split('&')

    if tool == '0+' and primary_subtype == 'default' and len(enchantments) > 0:
        item = 'tool_slot'
    else:
        item = tool

    if len(enchantments) == 0:
        ifs.append(workstation_state(item=item))
    else:
        for enchantment in enchantments:
            ifs.append(workstation_state(item=item, enchantments=[enchantment]))

    found_overrides = []
    for opt in tool_stanza:
        if opt == 'default' or opt == subtype:
            continue

        opt_parts = opt.split('/')
        primary_opt = opt_parts[0]
        
        opt_enchantments = []
        if primary_opt != 'default':
            opt_enchantments.append(primary_opt)
        
        if len(opt_parts) > 1:
            opt_enchantments = opt_enchantments + opt_parts[1].split('&')

        override_options = set(opt_enchantments) - set(enchantments) - set(found_overrides)

        for enchantment in override_options:
            unlesses.append(workstation_state(item=item, enchantments=[enchantment]))
            found_overrides.append(enchantment)


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
