"""
Generates the datapack.
"""

import os
import pathlib
import shutil
from inspect import getmembers, isfunction

import colorama 
from jinja2 import Environment, FileSystemLoader
from termcolor import colored

import grindless.config as config
import grindless.settings
from grindless.datapacks.grindless.templates import methods

colorama.init()

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

for func_name, fn in getmembers(methods, isfunction):
    env.globals[func_name] = fn

def build_all():
    """
    Builds the datapack
    """
    title = 'Grindless Minecraft Datapack :: Build'
    title_divider = '.'*20
    print(colored(f'{title_divider} {title} {title_divider}', 'magenta', 'on_grey', attrs=['bold']))
    
    print('\n')
    print(colored('1. Setting up directories', 'grey', 'on_white'))
    if os.path.isdir(config.DIST_DIR):
        status = colored(f'Removing previous build at {config.DIST_DIR}', 'white')
        print(status, '...', end="\r")
        shutil.rmtree(config.DIST_DIR)
        print(colored('DONE', 'green', attrs=['bold']), status)

    pathlib.Path(config.DIST_DIR).mkdir(parents=True, exist_ok=True)

    print('\n')
    print(colored('2. Getting Datapack Configs', 'grey', 'on_white'))
    datapack_configs = grindless.settings.fetch(from_console=True)

    print('\n')
    print(colored('3. Building Datapack', 'grey', 'on_white'))
    print(colored('3.1 General (Everything -Region Functions)', 'white', attrs=['bold']))
    build_general(datapack_configs)

    print('\n')
    print(colored('3.2 Region Functions', 'white', attrs=['bold']))
    build_regions(datapack_configs)

    print('\n')
    print(colored('Finished building datapack', color='green', attrs=['bold']))

def build_general(datapack_configs):
    """General build things

    Args:
        datapack_configs ([type]): [description]
    """
    skip_dirs = [
        '__pycache__',
        config.TEMPLATES_DIR,
        config.CONFIGS_DIR,
        config.SCFRIPTS_DIR,
    ]
    skip_files = [
        '__init__.py',
        'build.py',
        'config.py',
        'release.py',
        'helpers.py'
    ]

    for (dirpath, dirnames, filenames) in os.walk(config.SOURCE_DIR):
        skip = False
        
        for skip_dir in skip_dirs:
            if skip_dir in dirpath:
                skip = True
                break
        
        if skip:
            continue
        
        status = colored(f'Handling directory {dirpath}', 'white')
        print(status, '...', end='\r')
        output_dir = dirpath.replace(config.SOURCE_DIR, config.DIST_DIR)
        output_dir = output_dir.replace('/datapacks', '/data')
        print(status, '...', end='\r')
        pathlib.Path(output_dir).mkdir(parents=True, exist_ok=True)
        
        print(colored('DONE', 'green', attrs=['bold']), f'Created directory at {output_dir}')

        for f in filenames:
            if f in skip_files:
                continue
            
            print(f'Processing {f}...', end='\r')

            template_path = os.path.join(dirpath, f)
            # The template path is relative to the env.loader value (source_dir)
            template_path = template_path.replace(f"{config.SOURCE_DIR}/", '')
            template = env.get_template(template_path)
            
            output_file = f.replace('.j2', '')
            output_path = os.path.join(output_dir, output_file)

            print(colored(f'Rendering template {template_path}...', 'yellow'), end='\r')
            output = template.render(**datapack_configs)

            with open(output_path, "w") as fh:
                fh.write(output)
            
            print(colored('DONE', 'green', attrs=['bold']), f'Created file at {output_path}')

def build_regions(datapack_configs):
    region_template_path = config.REGION_TEMPLATE_PATH.replace(f"{config.SOURCE_DIR}/", '')
    region_template = env.get_template(region_template_path)

    pathlib.Path(config.DIST_REGION_FNS_DIR).mkdir(parents=True, exist_ok=True)
    print(colored('DONE', 'green', attrs=['bold']), f'Created directory at {config.DIST_REGION_FNS_DIR}')

    for region, region_config in datapack_configs['regions'].items():
        print(colored(f'Processing {region}...'), end='\r')

        output_path = os.path.join(config.DIST_REGION_FNS_DIR, f'{region}.mcfunction')
        output = region_template.render(**datapack_configs, region=region_config)

        with open(output_path, "w") as fh:
            fh.write(output)
            
        print(colored('DONE', 'green', attrs=['bold']), f'Created file at {output_path}')


if __name__ == '__main__':
    build_all()