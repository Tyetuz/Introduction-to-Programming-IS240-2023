#W12A1030AW.py
#Program to add two fractions and display their sum reduced to lowest terms.

import math #Import the math module to use the gcd function

def main(): #Main function to run the program
    try:
        fraction1 = get_fraction_input("first") #Get the first fraction input
        fraction2 = get_fraction_input("second") #Get the second fraction input
        result = fraction1 + fraction2 #Calculate the sum of the two fractions
        print(f"Sum: {result}") #Print the sum of the two fractions
    except Exception as e:
        print(f"An error occurred: {e}") #Handle any exceptions that occur

def get_fraction_input(fraction): #Handle the input of the fraction
    while True:
        try:
            numerator = int(input(f"Enter the numerator of the {fraction} fraction: ")) #Get the numerator of the fraction
            denominator = int(input(f"Enter the denominator of the {fraction} fraction: ")) #Get the denominator of the fraction
            return Fraction(numerator, denominator) #Return the fraction object
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.") #Handles invalid input

class Fraction:
    def __init__(self, numerator, denominator): #Constructor to initialize the fraction
        if denominator == 0:
            raise ValueError("Denominator cannot be zero.") #Handles division by zero
        self.numerator = numerator #Stores the numerator of the fraction
        self.denominator = denominator #Stores the denominator of the fraction
        self.reduce() #Store the fraction in reduced form
    
    def reduce(self): #Simplify the fraction to its lowest terms
        gcd = math.gcd(self.numerator, self.denominator)
        self.numerator //= gcd
        self.denominator //= gcd

    def add(self, other): #Add two fractions together store first fraction in self and second in other
        new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator) #New fraction object with the sum of the two fractions 
    
    def __add__(self, other: 'Fraction') -> 'Fraction': #Add method to allow direct addition of fractions stored in self and other
        return self.add(other) # 'Fraction') -> 'Fraction': #type hinting to specify the return type of the function
    
    def __str__(self): #Convert the fraction to a string
        return f"{self.numerator}/{self.denominator}"
    
main() #Call the main function to start the program