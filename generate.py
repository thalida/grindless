import os
import pathlib
import shutil
from jinja2 import Environment, FileSystemLoader
from inspect import getmembers, isfunction

import config
import helpers
import source.templates.methods as methods

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

if __name__ == '__main__': 
    datapack_configs = helpers.get_datapack_configs()

    if os.path.isdir(config.DIST_DIR):
        shutil.rmtree(config.DIST_DIR)

    pathlib.Path(config.DIST_DIR).mkdir(parents=True, exist_ok=True)

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