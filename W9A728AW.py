6#W9A728AW.py
#Program to calculate and display the factorial of a positive integer input by the user

def main(): #Every program starts with def main ():
    #Main entry point for the script calls functions n and factorial
    n = getN()
    factorial = fact(n)
    
    #Function to print: "n! is factorial"
    print(f"{n}! is {factorial}")
    
def getN():
    #Funtion to get a positive integer input from the user
    while True:
        try:
            n = int(input("Enter a positive integer: "))
            if n <= 0:
                print("Please enter a positive integer.")
                
            else:
                return n
        except ValueError:
            print("Invalid input! Please enter an integer.")
            
def fact(n):
    #Funtion to calculate the factorial
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

#Call the main function
main()


