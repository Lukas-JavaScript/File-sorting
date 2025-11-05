import os
import shutil as sh
from pathlib import Path

path = Path.cwd() 
def get_all_files(directory):
    return [f for f in directory.iterdir() if f.is_file()]

file_paths = get_all_files(path)

for file_path in file_paths:
    suffix = file_path.suffix.lower().strip(".") or "no_suffix"
    new_dir = path / suffix
    new_dir.mkdir(exist_ok=True)
    sh.move(str(file_path), str(new_dir / file_path.name))
    print(f"Moved: {file_path.name} -> {new_dir}")

input("Enter drücken ...")
