import os
import shutil

import GetInfo

def delete_files():
    show_options_delete_files()
    option = input("Option: ").lower()

    if option == "s":
        delete_single_files()
    elif option == "m":
        delete_multiple_files()
    elif option == "a":
        delete_all_files()
    else:
        print(f"The option {option} is not valid.")


def show_options_delete_files():
    print("\nChoose an option to delete files:")
    print("\ts - Single file ")
    print("\tm - Multiple files ")
    print("\ta - All the files ")


def delete(path_to_delete):
    if os.path.isfile(path_to_delete):  # 'path_to_delete' is a file
        os.remove(path_to_delete)
    else:                               # 'path_to_delete' is a directory
        shutil.rmtree(path_to_delete)


def delete_single_files():
    # Get path of the file 
    print("\nEnter the path of the file to delete: ")
    file_to_delete = GetInfo.get_file()
    if file_to_delete == "":
        return 1
    
    # Delete file
    delete(file_to_delete)

    print(f"File {file_to_delete} deleted successfully.")


def delete_multiple_files():
    # Get source and destiny directories' path
    print("\nEnter directory to detele files from.")
    dir_delete_from = GetInfo.get_dir()
    if dir_delete_from == "":
        return 1

    # Get list of files/directories to delete
    print("\nEnter the name of the files you want to delete from the directory.")
    num_of_files = len(os.listdir(dir_delete_from))
    files_to_delete = GetInfo.get_list_from_dir(num_of_files)

    # Delete files from the directory
    for file in os.listdir(dir_delete_from):
        path_to_delete = os.path.join(dir_delete_from, file)
        if file in files_to_delete:
            delete(path_to_delete)

    print(f"\nRequested files from {dir_delete_from} removed successfully.")


def delete_all_files():
    # Get directory's path
    print("\nEnter directory to delete all files from: ")
    dir_to_delete = GetInfo.get_dir()
    if dir_to_delete == "":
        return 1

    # Delete all files in the selected directory
    for file in os.listdir(dir_to_delete):
        delete(os.path.join(dir_to_delete, file))

    print(f"All files from {dir_to_delete} where deleted successfully.")
