import os

def showing_all_files():
        folder = []
        for i in os.listdir():
                if i.endswith(".txt"):
                        folder.append(i)
        if len(folder) > 0:
                print("Existing Text files are: ")
                for file in folder:
                        print(f"- {file}")
        else:
            print("There are no file in folder")
        return folder

def read_file():
    files = showing_all_files()
    if not files:
         return
    selected = input("Enter the exact file name you want to open: ")
    if selected not in files:
         print("There are no file in this name.")
         return
    try:
         with open(selected, "r") as reading:
              print(reading.read())
    except Exception as e:
         print("Something went wrong while reading the file:", e)

def write_file():
    files = showing_all_files()
    if not files:
         return
    selected = input("Enter the exact file name you want to Re-write: ")
    if selected not in files:
         print("There are no file in this name.")
         return
    try:
        new_content = input("Write your new content: ") 
        with open(selected, "w") as writing:
            writing.write(new_content)
        print("✅ Successfully re-written the privious text file.")
    except Exception as e:
        print("Something went wrong while write the file:", e)

def write_file_append_mode():
    files = showing_all_files()
    if not files:
         return
    selected = input("Enter the file name you want to append some text: ")
    if selected not in files:
         print("There are no file in this name.")
         return
    try:
        new_content = input("Write your new content: ") 
        with open(selected, "a") as writing:
            writing.write(new_content)
        print("✅ Successfully append text in file.")
    except Exception as e:
        print("Something went wrong while append some text in this file:", e)


def create_new_file():
    try:
        new = input("Write the file name(.txt): ")
        with open (new,'w') as new_file:
            take_input = input("Enter text: ")
            new_file.write(take_input)
        print(f"✅ Successfully file created and add some text")
    except Exception as info:
        print("Something is wrong",info)

def delete_a_file():
    files = showing_all_files()
    if not files:
        return
    selected = input("Enter the file-name which you want to delete: ")
    if selected not in files:
        print("⚠️ File not found.")
        return
    confirm = input(f"Are you sure you want to delete '{selected}'? (Y/N): ").lower()
    if confirm == 'y':
        try:
             os.remove(selected)
             print(f"🗑️ '{selected}' deleted successfully.")
        except Exception as e:
             print("Something went wrong while deleting the file:", e)
    else:
         print("❎ Deletion cancelled.")    


def main():
    while True:
        print('''
            1. Show all Existing file
            2. Read a file
            3. Re-write a file
            4. Append data in existing file
            5. Create new file
            6. Delete a file
            7. Exit the game
            ''')
        try:
            user_input = int(input("Select which you want: "))
        except ValueError: 
            print("Select specific one")
            continue

        if user_input == 1:
            showing_all_files()
        elif user_input == 2:
            read_file()
        elif user_input == 3:
             write_file()
        elif user_input == 4:
             write_file_append_mode()
        elif user_input == 5:
            create_new_file()
        elif user_input == 6:
            delete_a_file()
        elif user_input == 7:
            print("Exit the game!!")
            break
             
        else:
            print("Your enter the wrong selection")
        
        again = input("Do you restart the game(Y/N): ").lower()
        if again != "y":
            break

main()