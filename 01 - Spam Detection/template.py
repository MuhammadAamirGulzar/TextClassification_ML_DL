import os, sys
from pathlib import Path
import logging

while True:
    project_name = input("Enter project name: ")
    if project_name:
        break

# Create project directory and files
list_of_files = [
    f'{project_name}/__init__.py',
    f'{project_name}/main.py',
    f'{project_name}/README.md',
    f'{project_name}/requirements.txt',
    f'{project_name}/preprocessing/__init__.py',
    f'{project_name}/model/__init__.py',
    f'{project_name}/evaluate/__init__.py',
    f'{project_name}/config/__init__.py',
    f'{project_name}/utils/__init__.py'

]

# Create project directory and files if not exists already 
for file in list_of_files:
    file_path = Path(file)
    filedir , filename = os.path.split(file_path)    

    if not os.path.exists(filedir):
        os.makedirs(filedir)
        logging.info(f"Created directory: {filedir}")
    else:
        logging.info(f"Directory already exists: {filedir}")

    if not os.path.exists(file_path):
        with open(file_path, 'w') as f:
            f.write(f"# Path: {file_path}")
            logging.info(f"Created file: {file_path}")
    else:
        logging.info(f"File already exists: {file_path}")