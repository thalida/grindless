import os
import zipfile

import colorama 
from termcolor import colored

import config

if __name__ == '__main__':
    title = 'Grindless Minecraft Datapack :: Release Zip'
    title_divider = '.'*20
    print(colored(f'{title_divider} {title} {title_divider}', 'magenta', 'on_grey', attrs=['bold']))

    zip_name = f'chillcraft-v{config.VERSION}.zip'

    print('\n')
    print(colored(f'Creating {zip_name}...', 'cyan'))
    zipf = zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED)
    for root, dirs, files in os.walk(config.DIST_DIR):
        zip_root = root.replace(config.DIST_DIR, '')
        for f in files:
            print(f'Processing {f}...', end='\r')
            read_filepath = os.path.join(root, f)
            zip_filepath = os.path.join(zip_root, f)
            zipf.write(read_filepath, zip_filepath)
            print(colored('DONE', 'green', attrs=['bold']), f'Zipped file at {zip_filepath}')

    zipf.close()

    print('\n')
    print(colored(f'Finished zipping datapack: {zip_name}', color='green', attrs=['bold']))
