#Problem 36: Leap Year
#Program to determine if an entered year is a leap year

def is_leap_year(year):
    #Leap year is divisible by 4
    if (year % 4 == 0):
        #If the year is divisible by 100, it must also be divisible by 400
        if (year %100 == 0):
            if (year % 400 == 0):
                return True #It's a leap year
            else:
                return False #It's not a leap year
        
        else:
            return True #It's a leap year
    else:
        return False #It's not a leap year
    
#Function to check and print if the year is a leap year
def check_leap_year(input_year):
    #Check if year is a leap year
    if is_leap_year(input_year):
        return f"{input_year} is a leap year."
    else:
        return f"{input_year} is not a leap year."
    
#Request user input for the year
year = int(input("Enter a year: "))
result = check_leap_year(year)
print(result)

