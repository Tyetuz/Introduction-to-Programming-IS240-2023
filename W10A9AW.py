#W10A9AW.py
#Birthday dictonary program that looks up friends anf their birthdays

# Global dictionary containing names (Keys) and birthdays (Values)
BIRTHDAY_DICT = {
    'Hatley': 'January 1',
    'Stharlin': 'February 2',
    'Mikey': 'March 3',
    'Pete': 'April 4',
    'Latifa': 'May 5',
    'Kenny': 'June 6',
    'Kiara': 'July 7'
}

def main(): #  Main function to run the Birthday Dictionary Program.
    #Presents a menu of options and calls appropriate functions based on user input.
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")
        if choice == '1':
            lookup_birthday()
        elif choice == '2':
            add_birthday()
        elif choice == '3':
            change_birthday()
        elif choice == '4':
            delete_birthday()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

def display_menu():
    #Display the main menu options
    print("\nBirthday Dictionary Program")
    print("1. Look up a birthday")
    print("2. Add a new friend and birthday")
    print("3. Change a birthday")
    print("4. Delete a friend and birthday")
    print("5. Quit the program")

def lookup_birthday():
    # Look up and display a friend's birthday
    name = input("Enter the friend's name: ").strip().capitalize()
    print(f"{name}'s birthday is {BIRTHDAY_DICT.get(name, 'not found in the dictionary')}.")

def add_birthday():
    #Add a new friend and their birthday to the dictionary
    name = input("Enter the friend's name: ")
    birthday = input("Enter their birthday: ")
    BIRTHDAY_DICT[name] = birthday
    print(f"Added {name} with birthday {birthday}.")

def change_birthday():
    #Change an existing friend's birthday in the dictionary
    name = input("Enter the friend's name: ")
    if name in BIRTHDAY_DICT:
        BIRTHDAY_DICT[name] = input("Enter the new birthday: ")
        print(f"Updated {name}'s birthday.")
    else:
        print(f"{name} not found in the dictionary.")

def delete_birthday():
    #Delete a friend and their birthday from the dictionary
    name = input("Enter the friend's name: ")
    if name in BIRTHDAY_DICT:
        del BIRTHDAY_DICT[name]
        print(f"Deleted {name} from dictionary.")
    else:
        print(f"{name} not found in the dictionary.")
        

main()
        
