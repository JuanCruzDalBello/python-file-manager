import os

import GetInfo

def create(parts, path):
    if parts == 1:      # Create a directory
        os.mkdir(path)   
    else:               # Create file
        file = open(path, mode="x")
        file.close()

def create_file():

    print("\nEnter the path of the directory in which the new file will be created: ")
    path = GetInfo.get_dir()
    if path == "": return 1

    # New file's name, If there is no name return 1
    file_name = input("\nEnter the new file's name (file -> name.ext, dir -> name): ")
    if file_name in ["", " "]:
        print("File name can't be left blank.")
        return 1
    
    # Get full path
    full_path = os.path.join(path, file_name)

    # Create file
    # file_name.split = 1 -> dir | file_name.split = 2 -> file (file.extension)
    create(len(file_name.split(".")), full_path)
