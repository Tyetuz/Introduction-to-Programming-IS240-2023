#Problem 26: Radioactive Decay
# This program calculates the number of years required for 1 gram of Carbon-14 to decay to less than 1/2 gram

#Constants
initial_amount = 1.0 #Inital amount of Carbon-14
target_amount = initial_amount / 2 #Target amount
decay_rate = 0.00012 #.012% as a decimal

#Variables
current_amount = initial_amount
years = 0

#While loop to calculate the number of years for Carbon-14 to decay to half
while current_amount > target_amount:
    current_amount -= current_amount * decay_rate #Decrease the current amount based on the decay rate
    years += 1
    
#Output
print(f"Carbon-14 has a half-life of {years} years.")