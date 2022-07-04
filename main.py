import time

import CreateFiles
import ChangeName
import MoveFiles
import DeleteFiles

def menu():         # Prints program's menu
    print("\n--------------- File Manager ---------------")
    print("\nEnter a number from between 1 to 5 to select an option:")
    print("\t1. Create new file.")
    print("\t2. Change the name of a file.")
    print("\t3. Move file.")
    print("\t4. Delete File.")
    print("\t5. Exit the program.")


def main():
    while (True):
        menu()
        eleccion = input("\nEleccion: ")

        if eleccion == "1":
            CreateFiles.create_file()

        elif eleccion == "2":
            ChangeName.change_name()

        elif eleccion == "3":
            MoveFiles.move_files()

        elif eleccion == "4":
            DeleteFiles.delete_files()
        
        elif eleccion == "5":
            print("Thank you for using the program.")
            print("Shutting down 'File Manager'...")
            time.sleep(2)
            break

        else:
            print("\nOnly values from 1 to 5 are valid options.")

if __name__ == "__main__":
    main()