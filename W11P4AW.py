#W11P4AW.py
#Progam that creates a database and table in SQLite and runs an employee managment system.

import sqlite3
import datetime

def main(): #Main entry point for the script to run the employee management system. Handles user input and calls other functions.
    conn, cursor = create_database()
    while True:
        print("\nMenu:")
        print("1. Add an employee to the database")
        print("2. Archive an Employee")
        print("3. List all the Employees")
        print("4. Show all unarchived employees")
        print("5. Show all archived employees")
        print("6. Show all new employees who started their job on/or after 1/1/2017")
        print("7. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_employee(cursor, conn)
        elif choice == '2':
            archive_employee(cursor, conn)
        elif choice == '3':
            list_employees(cursor)
        elif choice == '4':
            show_unarchived_employees(cursor)
        elif choice == '5':
            show_archived_employees(cursor)
        elif choice == '6':
            show_new_employees(cursor)
        elif choice == '7':
            break
        else:
            print("Invalid choice. Please try again.")

def create_database(): #Create and connect to the SQLite database. Returns a connection and cursor object.
    conn = sqlite3.connect('Employee.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS employee_table (
        employeeID INTEGER PRIMARY KEY,
        firstName TEXT,
        lastName TEXT,
        salary REAL,
        yearStarted INTEGER,
        dob DATE,
        archived TEXT CHECK (archived IN ("Y", "N"))
    )''')
    conn.commit()
    return conn, cursor

def add_employee(cursor, conn): #Adds a new employee to the database. Prompts the user for employee details and Validates the input.
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    while True:
        try:
            salary = float(input("Enter salary: "))
            if salary < 0:
                raise ValueError("Salary cannot be negative.")
            break
        except ValueError as e:
            print(f"Invalid salary: {e}. Please enter a valid number.")
    while True:
        try:
            year_started = int(input("Enter year started: "))
            current_year = datetime.datetime.now().year
            if year_started < 1900 or year_started > current_year:
                raise ValueError(f"Year started must be between 1900 and {current_year}.")
            break
        except ValueError as e:
            print(f"Invalid year: {e}. Please enter a valid year.")
    while True:
        dob = input("Enter date of birth (yyyy-mm-dd): ")
        try:
            datetime.datetime.strptime(dob, "%Y-%m-%d")
            break
        except ValueError:
            print("Invalid date format. Please enter date in yyyy-mm-dd format.")
    archived = "N"
    cursor.execute('''INSERT INTO employee_table (firstName, lastName, salary, yearStarted, dob, archived)
                      VALUES (?, ?, ?, ?, ?, ?)''', (first_name, last_name, salary, year_started, dob, archived))
    conn.commit()
    print("Employee added successfully.")

def archive_employee(cursor, conn): #Archives an employee by updating the Archived column to "Y" for the specified employee ID.
    while True:
        try:
            employee_id = int(input("Enter employee ID to archive: "))
            break
        except ValueError:
            print("Invalid employee ID. Please enter a valid number.")
    cursor.execute('''UPDATE employee_table SET archived = "Y" WHERE employeeID = ?''', (employee_id,))
    conn.commit()
    print("Employee archived successfully.")

def list_employees(cursor): #Lists all employees in the database.
    cursor.execute('''SELECT * FROM employee_table''')
    employees = cursor.fetchall()
    print_employees(employees)

def show_unarchived_employees(cursor): #Shows all unarchived employees (Archived = "N").
    cursor.execute('''SELECT * FROM employee_table WHERE archived = "N"''')
    employees = cursor.fetchall()
    print_employees(employees)

def show_archived_employees(cursor): #Shows all archived employees (Archived = "Y").
    cursor.execute('''SELECT * FROM employee_table WHERE archived = "Y"''')
    employees = cursor.fetchall()
    print_employees(employees)

def show_new_employees(cursor): #Shows all new employees who started their job on or after 1/1/2017.
    cursor.execute('''SELECT * FROM employee_table WHERE yearStarted >= 2017''')
    employees = cursor.fetchall()
    print_employees(employees)

def print_employees(employees): #Print a formatted list of employees.
    # Print the header for the employee list
    print("ID    First Name     Last Name      Salary    Year Started   DOB         Archived")
    print("-------------------------------------------------------------------------------")
    
    # Print each employee's details
    for emp in employees:
        emp_id = emp[0]
        first_name = emp[1]
        last_name = emp[2]
        salary = emp[3]
        year_started = emp[4]
        dob = emp[5]
        archived = emp[6]
        
        # Print the employee details in a formatted way
        print(f"{emp_id:<5}{first_name:<15}{last_name:<15}${salary:<10.2f}{year_started:<15}{dob:<12}{archived:<10}")
        
#Call the main function to initiate the program
main()
