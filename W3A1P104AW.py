#Problem 104: Percentages
#Program to convert a percentage to a decimal.

def convert_percentage_to_decimal():
    #Input label
    percentage = float(input("Enter a percentage: "))
    
    #Convert percentage to a decimal
    decimal_value = percentage / 100
    
    #Output statement
    print(f"Equivalent decimal: {round(decimal_value, 2)}")
    
convert_percentage_to_decimal()