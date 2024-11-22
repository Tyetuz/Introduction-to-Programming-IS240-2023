#W9P3AW.py
#This program manages a list of colors with various operations such as adding, viewing, and removing colors.

#Global list of colors
colors = []

def main():
    #Main entry point for the script
    while True:
        choice = menu()
        if choice == 1:
            add_color()
        elif choice == 2:
            view_colors()
        elif choice == 3:
            color_starts_with()
        elif choice == 4:
            remove_color()
        elif choice == 5:
            print("Exiting the program.")
            break

def menu():
    #Function to display the menu and get the user's choice
    print("\nMenu:")
    print("1. Add a color to the list")
    print("2. View all colors in the list")
    print("3. View all colors in the list that begin with a letter")
    print("4. Remove a color")
    print("5. Exit")
    while True:
        try:
            choice = int(input("Pick a number from the menu: "))
            if 1 <= choice <= 5:
                return choice
            else:
                print("Invalid choice. Please pick a number from the menu.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def add_color():
    #Function to add a color to the list
    color = input("Enter the color you want to add: ").strip().lower()
    if if_exists(color):
        print(f"The color '{color}' already exists.")
    else:
        colors.append(color)
        print(f"The color '{color}' has been added.")

def view_colors():
    #Function to view all colors in alphabetical order
    if colors:
        for color in sorted(colors):
            print(color)
    else:
        print("No colors in the list.")

def color_starts_with():
    #Function to view colors that start with a specific letter
    letter = input("Enter the letter you want the colors to start with: ").strip().lower()
    filtered_colors = [color for color in colors if color.startswith(letter)]
    if filtered_colors:
        for color in filtered_colors:
            print(color)
        print(f"There are {len(filtered_colors)} colors that begin with '{letter}'.")
    else:
        print(f"Sorry, no colors begin with the letter '{letter}'.")

def remove_color():
    #Function to remove a color from the list
    color = input("Enter the color you want to remove: ").strip().lower()
    if if_exists(color):
        colors.remove(color)
        print(f"The color '{color}' has been removed.")
    else:
        print(f"The color '{color}' does not exist and cannot be removed.")

def if_exists(color):
    #Boolean function to check if a color exists in the list
    return color in colors

#Main function call
main()
