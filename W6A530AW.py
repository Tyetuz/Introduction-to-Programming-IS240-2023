#Problem 30: Cooling
#This program will determine the number of minutes required for the coffee to cool below 150 F

#Constants
initial_temperature = 212 #Initial temperature of the coffee
room_temperature = 70 #Room temperature
k = 0.079 #Cooling constant
target_temperature = 150 #Target temperature

#Variables
current_temperature = initial_temperature
minutes = 0

#While loop to calculate the number of minutes to cool the coffee
while current_temperature > target_temperature:
    temperature_decrease = k * (current_temperature - room_temperature) #Calculate the temperature decrease
    current_temperature -= temperature_decrease #Update the current temperature
    minutes += 1 #Increment the minutes


#Output
print(f"The coffee will cool to below {target_temperature} degrees in {minutes} minutes.")