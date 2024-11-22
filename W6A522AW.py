#Problem 22: Consumer Price Index
#This program calculates the future Consumer Price Index (CPI) based on an initial value and growth rate.

#Initial CPI value
cpi_july_2014 = 238.25 #CPI in July 2014
annual_growth_rate = 0.025 # Anuual growth rate of CPI

cpi = cpi_july_2014
years = 0

#Target CPI is double the July 2014 CPI
target_cpi = cpi_july_2014 * 2

#While loop to calculate the number of years needed for CPI to double
while cpi < target_cpi:
    cpi *= (1 + annual_growth_rate) #Update CPI based on growth rate
    years += 1
    
#Output Results
print(f"Consumer prices will double in {years} years.")