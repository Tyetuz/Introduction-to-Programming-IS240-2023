#Problem 28: Cost of Copies
#Program to calculate the total cost of copies
#With varying fees based on the number of copies

def calculate_cost_of_copies(copies):
    #Cost variables
    base_cost = 0.05 #Cost for first 100 copies
    additional_cost = 0.03 #Cost for additional copies
    total_cost = 0.0
    
    #Check the number of copies to calculate total cost
    if copies < 100:
        total_cost = copies * base_cost
        
    else:
        #Calculate cost for first 100 and additional copies
        total_cost = (100 * base_cost) + ((copies - 100) * additional_cost)
    
    return total_cost

#Input for the number of copies
number_of_copies = int(input("How many copies would you like?: "))

#Calculate total cost
cost = calculate_cost_of_copies(number_of_copies)

#Output
print(f"Enter number of copies:{number_of_copies}")
print(f"Cost is ${cost:.2f}")
    