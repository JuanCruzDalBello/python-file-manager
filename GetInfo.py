import os

def get_file():
    # Return a file path if it exists
    file = input("\nFile path: ")
    if not os.path.exists(file):
        print(f"The file {file} doesn't exist.")
        return ""
    return file


def get_dir():
    # Return a dir path if it exists
    dir = input("\nDir path: ")
    if not os.path.isdir(dir):
        print(f"{dir} is not a valid directory.")
        return ""
    return dir


def get_list_from_dir(num_of_files):
    # Takes strings from the user and returns a list with all of them
    # Takes as many inputs as files inside a directory (num_of_files)
    # Stop the input when the user enters nothing
    list_files = []
    print("To stop the input press enter without writting anything.")
    for i in range(num_of_files):
        file = input("File: ")
        if file == "" : break
        list_files.append(file)
    return list_files
    