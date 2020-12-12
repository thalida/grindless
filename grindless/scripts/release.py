"""
.. _scripts-release:

.. important::
    You'll need to create a build before running this script, see :ref:`build script <scripts-build>` docs for more info.

Release
======================

Zips a build of the datapack for easy sharing / releasing.

Usage
-----------------------

>>> cd /abs/path/to/grindless-repo
>>> python -m grindless.scripts.release
Zips the datapack dist folder

Functions
----------------------------
.. autofunction:: grindless.scripts.release.release

"""


import os
import pathlib
import zipfile

import colorama 
from termcolor import colored

import grindless.config as config
import grindless.settings

def release():
    """
    Creates a zipped release verion of the conents of the datapack DIST directory.
    """
    title = 'Grindless Minecraft Datapack :: Release Zip'
    title_divider = '.'*20
    print(colored(f'{title_divider} {title} {title_divider}', 'magenta', 'on_grey', attrs=['bold']))
    
    datapack_settings = grindless.settings.fetch(yaml_only=True)
    # Create the zip name based on the datapack namesapce and current version
    zip_name = f"{datapack_settings['global']['namespace']}-v{config.VERSION}.zip"

    print('\n')
    print(colored(f'Creating {zip_name}...', 'cyan'))
    
    # Make sure the zip output directory exists
    pathlib.Path(config.ZIPS_DIR).mkdir(parents=True, exist_ok=True)
    # Create the full zip path including filename (zipname)
    zip_path = os.path.join(config.ZIPS_DIR, zip_name)

    # Use the builtin zip library to create a zip file we'll add files to
    zipf = zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED)

    # Walk the dist directory and add each folder + file to the zip
    for root, dirs, files in os.walk(config.DIST_DIR):
        # Let's have the zip folders be relative to the dist dir
        #   without this the entire folder tree from root would be created in the dist.
        zip_root = root.replace(config.DIST_DIR, '')
        
        # Loop over each file we've walked over, and output it to he dist
        for f in files:
            print(f'Processing {f}...', end='\r')
            read_filepath = os.path.join(root, f)
            zip_filepath = os.path.join(zip_root, f)
            zipf.write(read_filepath, zip_filepath)
            print(colored('DONE', 'green', attrs=['bold']), f'Zipped file at {zip_filepath}')

    zipf.close()
    # Annnd we're don! Zip should have been created in the release folder.

    print('\n')
    print(colored(f'Finished zipping datapack: {zip_name}', color='green', attrs=['bold']))


if __name__ == '__main__':
    release()