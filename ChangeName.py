import os

import GetInfo

def change_name():
    # Get path of the file, if the file doesn't exist return 1
    print("\nEnter the path of the file/directory you want to change the name of: ")
    old_name_path = GetInfo.get_file()
    if old_name_path == "":
        return 1

    # Keep the file extention the same
    file_extention = "." + (os.path.basename(old_name_path)).split(".")[1]
    new_name = input("\nEnter new name: ")
    new_name += file_extention

    # Get path of the new name file
    new_name_path = os.path.join(os.path.dirname(old_name_path), new_name)

    # Rename the file
    os.rename(old_name_path, new_name_path)

    print(f"File name changed successfully. New name = {new_name_path}")