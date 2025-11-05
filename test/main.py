import os
import shutil as sh
from pathlib import Path
import sys 

path = Path(sys.executable).parent
file_paths = []

def get_all_files(path):
    for file in path.iterdir():
        if file.is_file():
            file_paths.append(file)
get_all_files(path)

for file in file_paths:
    file_path = Path(file)
    suffix = file.suffix.lower().strip(".")
    name = file.name
    if not suffix:
        suffix = "no_suffix"  
    # Zielverzeichnis erstellen
    new_dir = path / suffix / file_path.name
    new_dir.parent.mkdir(parents=True, exist_ok=True)
    # Datei verschieben
    sh.move(file_path, new_dir)
