# W9A868AW.py
# Program to calculate monthly mortgage values

def main():
    interest_rate, monthly_payment, beginning_balance = get_inputs() #Get user inputs for interest rate, monthly payment and beginning balance
    interest_paid, principal_reduction, end_balance = calculate_values(interest_rate, monthly_payment, beginning_balance) #Calculations
    display_results(interest_paid, principal_reduction, end_balance) #Display the results of the stored variables

def get_inputs():
    interest_rate = float(input("Enter annual rate of interest: ")) / 100 #Prompts user for interest rate and converts to decimal
    monthly_payment = float(input("Enter monthly payment: ")) #Prompt user for monthly payment amount
    beginning_balance = float(input("Enter beginning of month balance: ")) #Prompt user for the beginning balance
    return interest_rate, monthly_payment, beginning_balance

def calculate_values(interest_rate, monthly_payment, beginning_balance):
    monthly_rate = interest_rate / 12 #Calculate monthly interest rate
    interest_paid = monthly_rate * beginning_balance #Calculate interest paid for the month
    principal_reduction = monthly_payment - interest_paid #Calculate principal reduction
    end_balance = beginning_balance - principal_reduction #Calculate end of the month balance
    return interest_paid, principal_reduction, end_balance #Return calculated values

def display_results(interest_paid, principal_reduction, end_balance):
    print(f"Interest paid for the month: ${interest_paid:,.2f}")
    print(f"Reduction of principal: ${principal_reduction:,.2f}")
    print(f"End of month balance: ${end_balance:,.2f}")
    
main() #Calling main to run program
