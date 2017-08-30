'''

This script will compile py to pyc files, so the way it works is
    1. Create a working directory which contains a folder "py_files"
    2. Inside "py_files" folder place all the py files
    3. we will use shutil module which will create another folder named "pyc_files"
    4. All the py files from "py_files" folder will be moved into "pyc_files" folder
    5. After copying all py file, using compileall will convert py files in "pyc_files" folder to pyc files

'''

import compileall
import shutil
import os

src_dir = "py_files"
des_dir = "pyc_files"

# Get current working directory
pyc_dir = os.getcwd()
pyc_dir = os.path.join(pyc_dir, des_dir)

# check if a folder named "pyc_files" exists if so removed it and recreate a new one
if os.path.exists(des_dir):
    shutil.rmtree(des_dir)

shutil.copytree(src_dir, des_dir)

# Compiles all python files to pyc
compileall.compile_dir(pyc_dir, force=True)

for file_name in os.listdir(des_dir):
    if file_name.endswith(".py"):
        os.remove(os.path.join(pyc_dir, file_name))


