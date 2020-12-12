"""
.. important::
    Make sure you've completed all the steps 
    in :ref:`Getting Started <getting-started>` before running!

.. _scripts-build:

Build
======================

Compiles and outputs the datapack.


Usage
-----------------------

>>> cd /abs/path/to/grindless-repo
>>> python -m grindless.scripts.build
Runs datapack build


Functions
----------------------------
.. autofunction:: grindless.scripts.build.build
.. autofunction:: grindless.scripts.build.build_general
.. autofunction:: grindless.scripts.build.build_regions


Jinja Environment
------------------------
Setup
^^^^^^^^^^^^^^^^^^^^^^^^
.. autodata:: grindless.scripts.build.env

.. rubric:: ``env`` declaration:
.. literalinclude:: /../grindless/scripts/build.py
    :lines: 66-77

Options
^^^^^^^^^^^^^^^^^^^^^^^^^
The docs for a Jinja2 Environment are included below, but the `Official Jinja Docs <https://jinja.palletsprojects.com>`_ should be the primary reference.

.. autodata:: jinja2.Environment

"""

# Builtins
import os
import pathlib
import shutil
from inspect import getmembers, isfunction

# Third-party
import colorama 
from jinja2 import Environment, FileSystemLoader
from termcolor import colored
colorama.init()

# Internal
import grindless.config as config
import grindless.settings
from grindless.datapacks.grindless.templates import methods

#: An instance of a Jinja2 Environment.
#: The environment globals are extended to include the datapack's custom template methods
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

def build(prints_enabled=False):
    """
    Main build script for the datapack. 
    This script calls build_general() and build_regions().
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
    datapack_settings = grindless.settings.fetch(prints_enabled=prints_enabled)

    print('\n')
    print(colored('3. Building Datapack', 'grey', 'on_white'))
    print(colored('3.1 General (Everything -Region Functions)', 'white', attrs=['bold']))
    build_general(datapack_settings)

    print('\n')
    print(colored('3.2 Region Functions', 'white', attrs=['bold']))
    build_regions(datapack_settings)

    print('\n')
    print(colored('Finished building datapack', color='green', attrs=['bold']))

def build_general(datapack_settings):
    """Builds all non-region files. This is the default build script for most of the datapack.

    Args:
        datapack_settings (dict): formatted datapack settings
    """

    #: These directories should not be built
    skip_dirs = [
        '__pycache__',
        config.TEMPLATES_DIR,
        config.SETTINGS_DIR,
        config.SCRIPTS_DIR,
    ]

    #: These files should not be included in the build
    skip_files = [
        '__init__.py',
        'config.py',
        'helpers.py'
    ]

    # Loop over all the file in the SOURCE_DIR
    for (dirpath, dirnames, filenames) in os.walk(config.SOURCE_DIR):
        skip = False
        
        # Check if the current directory is part of any of the skipped dirs
        for skip_dir in skip_dirs:
            if skip_dir in dirpath:
                skip = True
                break
        
        if skip:
            continue
        
        status = colored(f'Handling directory {dirpath}', 'white')
        print(status, '...', end='\r')
        
        # Setup the output directory path to point to the dist directory
        output_dir = dirpath.replace(config.SOURCE_DIR, config.DIST_DIR)
        # Minecraft requires datapack logic to be in a data folder. Let's make that change now.
        output_dir = output_dir.replace('/datapacks', '/data')

        # Let's make sure that directory path exists (and the entire tree is created: parents=True)
        pathlib.Path(output_dir).mkdir(parents=True, exist_ok=True)
        
        print(colored('DONE', 'green', attrs=['bold']), f'Created directory at {output_dir}')

        # If we've walked over some files, let's process those now...
        for f in filenames:
            # Well first we skip files we don't need in the final build
            if f in skip_files:
                continue
            
            print(f'Processing {f}...', end='\r')
            
            # Create the fullpath to this file (template)
            template_path = os.path.join(dirpath, f)
            # Make the path relative to the env.loader value (source_dir) for jinja to work correctly.
            template_path = template_path.replace(f"{config.SOURCE_DIR}/", '')
            # With a now, jinja approved template path, let's get the template.
            # It's okay(-ish) if the file actually isn't jinja.
            template = env.get_template(template_path)

            # The output file should not incldue the .j2 (jinja2) extension
            output_file = f.replace('.j2', '')
            # The full output path should use our process output dir from earlier
            output_path = os.path.join(output_dir, output_file)

            print(colored(f'Rendering template {template_path}...', 'yellow'), end='\r')
            # Here we go! Rendering the file/template with our datapack settings
            output = template.render(**datapack_settings)
            
            # We write the output to the file we created.
            with open(output_path, "w") as fh:
                fh.write(output)

            # With that one file has been built and output! Let's continue..
            print(colored('DONE', 'green', attrs=['bold']), f'Created file at {output_path}')


def build_regions(datapack_settings):
    """Builds and outputs all of the region datapack functions.

    Args:
        datapack_settings (dict): formatted datapack settings
    """
    
    #: Each region uses the same base template for rendering it's .mcfunction file
    region_template_path = config.REGION_TEMPLATE_PATH.replace(f"{config.SOURCE_DIR}/", '')
    #: Use jinja to fetch the template; This is used for rendering later.
    region_template = env.get_template(region_template_path)

    # Make sure the regions dist directory is exists.
    pathlib.Path(config.DIST_REGION_FNS_DIR).mkdir(parents=True, exist_ok=True)
    print(colored('DONE', 'green', attrs=['bold']), f'Created directory at {config.DIST_REGION_FNS_DIR}')

    # For each for the regions defined in our settings...
    for region, region_config in datapack_settings['regions'].items():
        print(colored(f'Processing {region}...'), end='\r')
    
        # Setup the output path for the region mcfunction
        output_path = os.path.join(config.DIST_REGION_FNS_DIR, f'{region}.mcfunction')
        # Render the region template given this regions settings
        output = region_template.render(**datapack_settings, region=region_config)
        # Write the output to the filesystem
        with open(output_path, "w") as fh:
            fh.write(output)
        
        print(colored('DONE', 'green', attrs=['bold']), f'Created file at {output_path}')
        # Rinse and repeat!


if __name__ == '__main__':
    # If we're running this script from the commandline, run the entire build!
    build(prints_enabled=True)