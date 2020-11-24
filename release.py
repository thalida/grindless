import os
import zipfile

import config

if __name__ == '__main__':
    zipf = zipfile.ZipFile(f'chillcraft-v{config.VERSION}.zip', 'w', zipfile.ZIP_DEFLATED)
    for root, dirs, files in os.walk(config.DIST_DIR):
        zip_root = root.replace(config.DIST_DIR, '')

        for f in files:
            read_filepath = os.path.join(root, f)
            zip_filepath = os.path.join(zip_root, f)
            zipf.write(read_filepath, zip_filepath)

    zipf.close()