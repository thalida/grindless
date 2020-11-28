import os
import pathlib
import shutil
from jinja2 import Environment, FileSystemLoader
from inspect import getmembers, isfunction

import config
import helpers
import source.templates.methods as methods


datapack_configs = helpers.get_datapack_configs()

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

def build_general():
    for (dirpath, dirnames, filenames) in os.walk(config.SOURCE_DIR):
        if (config.TEMPLATES_DIR in dirpath) or (config.CONFIGS_DIR in dirpath):
            continue
        
        output_dir = dirpath.replace(config.SOURCE_DIR, config.DIST_DIR)
        pathlib.Path(output_dir).mkdir(parents=True, exist_ok=True)

        for f in filenames:
            template_path = os.path.join(dirpath, f)
            template_path = template_path.replace(f"{config.SOURCE_DIR}/", '')
            template = env.get_template(template_path)
            
            output_file = f.replace('.j2', '')
            output_path = os.path.join(output_dir, output_file)
            output = template.render(**datapack_configs)

            with open(output_path, "w") as fh:
                fh.write(output)

def build_regions():
    region_template_path = config.REGION_TEMPLATE_PATH.replace(f"{config.SOURCE_DIR}/", '')
    region_template = env.get_template(region_template_path)

    pathlib.Path(config.DIST_REGION_FNS_DIR).mkdir(parents=True, exist_ok=True)
    for region in datapack_configs['gather']['enabled_regions']:
        output_path = os.path.join(config.DIST_REGION_FNS_DIR, f'{region}.mcfunction')
        output = region_template.render(**datapack_configs, region=datapack_configs['regions'][region])

        with open(output_path, "w") as fh:
            fh.write(output)

def run_build():
    if os.path.isdir(config.DIST_DIR):
        shutil.rmtree(config.DIST_DIR)

    pathlib.Path(config.DIST_DIR).mkdir(parents=True, exist_ok=True)

    build_general()
    build_regions()

if __name__ == '__main__':
    run_build()