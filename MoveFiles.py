import os
import shutil

import GetInfo

def move_files():
    show_options_move_files()
    option = input("Option: ").lower()

    if option == "s":
        move_single_file()
    elif option == "m":
        move_multiple_files()
    elif option == "a":
        move_all_file()
    else:
        print(f"The option {option} is not valid.")


def show_options_move_files():    # Shows aditional options from main menu option "Move file" 
    print("\nChoose an option to move files:")
    print("\ts - Single file ")
    print("\tm - Multiple files ")
    print("\ta - All the files ")


def delete(path_to_delete):
    if os.path.isfile(path_to_delete):  # 'path_to_delete' is a file
        os.remove(path_to_delete)
    else:                               # 'path_to_delete' is a directory
        shutil.rmtree(path_to_delete)


def already_there(path_to_move, dest_path):
    # Loop through the destiny path to check if the file is not there already
    dest_path_list = os.listdir(os.path.dirname(dest_path))
    file_to_move = os.path.basename(path_to_move)
    for file in dest_path_list:
        if file == file_to_move:
            return True


def move(path_to_move, dest_path):
    if not already_there(path_to_move, dest_path):
        if os.path.isfile(path_to_move):    # 'path_to_copy' is a file
            shutil.copy(
                path_to_move,
                dest_path
            )
        else:                               # 'path_to_copy' is a directory
            shutil.copytree(
                path_to_move,
                dest_path
            )


########################################


def move_single_file():
    # Get source and destiny files' path 
    print("\nEnter the path of the file you want to move.")
    source_file_path = GetInfo.get_file()

    print("\nEnter the path of the directory to move to.")
    dest_file_path = GetInfo.get_dir()

    # If paths are empty return 1 as error.
    if source_file_path == "" or dest_file_path == "":
        return 1

    # Create the path of the newly created file
    dest_file_path = os.path.join(
                            dest_file_path,
                            os.path.basename(source_file_path)
                        )

    # Copy the original file to selected location
    move(source_file_path, dest_file_path)

    # Delete original file
    delete(source_file_path)

    print(f"\nFile copied successfully at {dest_file_path}")


def move_multiple_files():
    # Get source and destiny directories' path
    print("\nEnter the path of the directory to move files from.")
    source_dir = GetInfo.get_dir()
        
    print("\nEnter the path of the directory to move to.")
    dest_dir = GetInfo.get_dir()

    # If paths are empty return 1 as error.
    if source_dir == "" or dest_dir == "":
        return 1

    # Get list of files/directories to move
    print(f"\nEnter the name of the files you want to move to {dest_dir}.")
    num_of_files = len(os.listdir(source_dir))
    files_to_move = GetInfo.get_list_from_dir(num_of_files)

    # Move files in files_to_move to the dest directory 
    for file in os.listdir(source_dir):
        path_to_move = os.path.join(source_dir, file)
        dest_path = os.path.join(dest_dir, file)
        if file in files_to_move:
            move(path_to_move, dest_path)

    # Delete files from the source directory
    for file in os.listdir(source_dir):
        if file in files_to_move:
            path_to_delete = os.path.join(source_dir, file)
            delete(path_to_delete)

    print(f"\nRequested files from {source_dir} moved to {dest_dir} successfully.")
    print(f"Moved files:")
    for file in files_to_move:
        print(f"\t- {file}")


def move_all_file():
    # Get source and destiny directories' path
    print("\nEnter directory to copy all files from: ")
    source_dir = GetInfo.get_dir()

    print("\nEnter directory to copy all files to: ")
    dest_dir = GetInfo.get_dir()

    # If paths are empty return 1 as error.
    if source_dir == "" or dest_dir == "":
        return 1

    # Move one by one all the files from the source directory to the destiny directory
    for file in os.listdir(source_dir):
        path_to_copy = os.path.join(source_dir, file)
        dest_path = os.path.join(dest_dir, file)
        move(path_to_copy, dest_path)

    # Delete files from the source directory
    # TODO: cambiar por funcion deletePath() mas generalizada
    for file in os.listdir(source_dir):
        path_to_delete = os.path.join(source_dir, file)
        delete(path_to_delete)

    print(f"\nAll files from {source_dir} moved to {dest_dir} successfully.")