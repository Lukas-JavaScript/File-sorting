import os
import shutil as sh
from pathlib import Path
import sys 

path = Path(sys.executable).parent
file_paths = []

def get_all_files(path):
    for file in path.iterdir():
        for file in file:
            file_paths.append(os.path.join(path, file))
    return file_paths
