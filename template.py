import os, sys
from pathlib import Path
import logging

while True:
    project_name = input("Enter project name: ")
    if project_name != "":
        break


list_of_files=[
    f"{project_name}/__init__.py",
    f"{project_name}/config/__init__.py",
    f"{project_name}/preprocessing/__init__.py",
    f"{project_name}/model/__init__.py",
    


]