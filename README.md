# File sorting

This script moves all files within a specific directory, categorizing them into subfolders based on their file extensions.

## 🪄 Installation Instructions:

1. Ensure that Python is installed on your system.
2. Clone or download the repository.
3. Open a command prompt or terminal and navigate to the downloaded directory.

## 🚀 Usage:

The script operates as follows:

1. It imports necessary modules: os, shutil, and pathlib.
2. Defines the current working directory using Path.cwd().
3. Defines a function get_all_files(directory) that returns a list of all files in the specified directory.
4. Calls the function with get_all_files(path) to obtain a list of file paths, which is stored in file_paths.
5. Iterates over each file in file_paths:
- Extracts the file suffix (after the period).
- Creates a subfolder based on the suffix if it does not already exist.
- Moves the file into the corresponding subfolder using sh.move().
6. It outputs a message indicating the move operation for each file.

## 🧠 Example:

If the current working directory contains files such as file1.txt, file2.pdf, and image.jpg, these would be moved into subfolders named txt/, pdf/, and jpg/ respectively, based on their file extensions.

## 🧠 Notes:

- The script moves all files in the specified directory and its subdirectories.
- It retains the original filename while moving and creates folders based on the file suffix.
- Ensure that no important files are present in the target directory that might be affected by this script.

## 🛡️ License:

This project is licensed under the MIT license - see the LICENSE file for details.

