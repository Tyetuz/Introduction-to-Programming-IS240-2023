#Problem 68: Median Calculation
#Function to calculate the median of a list of numbers

def calculate_median(numbers):
    numbers.sort() #Sort the list of numbers
    n = len(numbers) #Find the length of the list
    if n % 2 == 1: #Check if the number of measurments is odd
        return numbers[n // 2] #Return the middle measurement
    else:
        #Return the average of the two middle measurements
        mid1 = numbers[n // 2 - 1]
        mid2 = numbers[n // 2]
        return (mid1 + mid2) / 2
    
#Request the number of measurements from the user
n = int(input("How many numbers do you want to enter? "))
measurements = [] #An empty list to store the measurements

#For loop to request each measurement from the user
for i in range(n):
    number = float(input(f"Enter number {i + 1}: "))
    measurements.append(number)
    
#Calculate the median of the measurements
median = calculate_median(measurements)

#Display the median
print(f"Median: {median}")