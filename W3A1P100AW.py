#Problem 100: Cost of Electricity
#Program to calculate the cost of operating an electrical device.

def calculate_electricity_cost():
    #Input labels
    wattage = float(input("Enter the wattage of the device: "))
    hours_used = float(input("Enter the number of hours the device is used: "))
    cost_per_kwh = 11.76 #Cost per kWh in cents
    
    #Convert cost from cents to dollars
    cost_per_kwh_dollars = cost_per_kwh / 100
    
    #Calculate the cost of electricity
    cost_of_electricity = (wattage * hours_used) / 1000 * cost_per_kwh_dollars
    
    #Output Statement
    print(f"Cost of electricity: ${round(cost_of_electricity, 2)}")
    
calculate_electricity_cost()
    
    