__winc_id__ = 'ae539110d03e49ea8738fd413ac44ba8'
__human_name__ = 'files'


# imported modules:
import os
import shutil
import zipfile
from zipfile import ZipFile


current_directory = os.getcwd()
folder = 'cache'
cache_dir_path = current_directory + '//cache'
zip_file_path = current_directory + '//data.zip'


# 1:
def clean_cache():
    try:
        os.mkdir(folder)
        print("Directory " , folder ,  " Created ") 
    except FileExistsError:
        shutil.rmtree(folder)
        os.mkdir(folder)
        print("Directory", folder , "deleted and created again")
        

# 2:
def cache_zip(zip_file_path, cache_dir_path):
    clean_cache()
    with zipfile.ZipFile(zip_file_path, 'r') as data:
        data.extractall(cache_dir_path)
    print('data.zip unpacked')
     

# 3:
def cached_files():
    path = os.path.abspath("cache")
    return [entry.path for entry in os.scandir(path) if entry.is_file()]


# 4:
def find_password(cached_files):
    for file in cached_files:
        with open(file) as file_data:
            file_datalist = file_data.readlines()
            for target in file_datalist:
                if "password" in target:
                    password = target.split(" ")[-1].strip()
                    return password



