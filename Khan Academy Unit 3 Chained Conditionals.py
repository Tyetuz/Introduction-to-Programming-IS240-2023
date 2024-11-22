day_of_the_week = input("What day of the week is it today? ")

if day_of_the_week == "Saturday" or day_of_the_week == "Sunday":
    print("We're open from 11-2 today")
else:
    print("We're open from 9-3 today")

screen_width = float(input("How wide is the screen in pixels? "))

if screen_width < 100:
    print("Empty layout")
elif screen_width < 320:
    print("Mobile layout")
elif screen_width < 760:
    print("Tablet layout")
else:
    print("Desktop layout") 

print("Loading display...")