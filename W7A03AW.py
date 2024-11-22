#Problem 3: Caffeine Absorption
#Program calculating 13% of caffeine consumed is eliminated from the body each hour

def caffeine_absorption():
    initial_caffeine = 130  #Mg of caffeine in one cup of coffee
    elimination_rate = 0.13 #13% elimination per hour
    
    print(f"CAFFEINE VALUES")
    
    #Part (a): Calculate the hours until caffeine level drops below 65 mg
    caffeine = initial_caffeine
    hours = 0
    while caffeine >= 65:
        caffeine -= caffeine * elimination_rate #Eliminate 13% of current caffeine per hour
        hours += 1
    print(f"One cup: less than 65 mg. will remain after {hours} hours.")
    
    #Part (b): Calculate the amount of caffeine remaining after 24 hours
    caffeine = initial_caffeine
    for i in range(24):
        caffeine -= caffeine * elimination_rate  #Eliminate 13% of current caffeine per hour
    print(f"One cup: {caffeine:.2f} mg. will remain after 24 hours.")
    
    #Part (c): Calculate caffeine levels after drinking one cup every hour for 24 hours
    caffeine = 0
    for hour in range(25): #loop runs 25 times, simulating 24 hours and one additional hour to account for the last cup of coffee
        caffeine -= caffeine * elimination_rate #Eliminate 13% of current caffeine
        caffeine += initial_caffeine #Add a new cup of coffee
    print(f"Hourly cups: {caffeine:.2f} mg. will remain after 24 hours.")
    
#Run the function to see the results
caffeine_absorption()