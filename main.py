import os
from shutil import copy

def scraper_files(origin_folder, destiny_folder, select_files, type_file):

    if not os.path.exists(destiny_folder):
        os.makedirs(destiny_folder)

    for file in os.listdir(origin_folder):
        if any(file.startswith(file_sel) for file_sel in select_files) and file.endswith(type_file):
            origin_path = os.path.join(origin_folder, file)
            destiny_path = os.path.join(destiny_folder, file)
            
            copy(origin_path, destiny_path)
            print('copied')

origin_folder = './origin'
destiny_folder = './destiny'
files = ['text_01', 'text_02']
type_file = '.txt'

print(origin_folder, destiny_folder, files, type_file)

scraper_files(origin_folder, destiny_folder, files, type_file)