#Problem 112: Convert Lengths
#Program to convert inches to feet and inches

def convert_inches_to_feet_and_inches():
    #Input label
    total_inches = int(input("Enter a whole number of inches: "))
    
    #Use integer division to get feet and modulus to get remaining inches
    feet = total_inches // 12
    inches = total_inches % 12
    
    #Output Statement
    print(f"{total_inches} inches is {feet} feet and {inches} inches.")
    
convert_inches_to_feet_and_inches()    