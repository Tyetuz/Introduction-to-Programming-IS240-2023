#Problem 56
#Function to calculate new salary after raise

def calculate_new_salary(beginning_salary):
    #Rate of raise
    raise_rate = 0.05
    #Calculating new salary after three raises
    new_salary = beginning_salary * (1 + raise_rate) ** 3
    return new_salary

#Funtion to calculate percentage change

def calculate_percentage_change(beginning_salary, new_salary):
    #Percentage change formula
    change = (new_salary - beginning_salary) / beginning_salary * 100
    return change

#Main
def main():
    #Requesting beginning salary from user
    beginning_salary = float(input("Enter beginning salary: "))
    #Calculate new salary
    new_salary = calculate_new_salary(beginning_salary)
    #Calculating percentage change
    change = calculate_percentage_change(beginning_salary, new_salary)
    
    #Display results with formatting
    print(f'New salary:${new_salary:,.2f}')
    print(f'Change:{change:.2f}%')
    
main()