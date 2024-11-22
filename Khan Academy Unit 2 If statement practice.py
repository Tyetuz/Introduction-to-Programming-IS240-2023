num_orders = 10

if num_orders == 10:
    print("Your order is free!")
    num_orders = 0
print(num_orders)

order = input("What would you like to order? ")
protein = "No protein"
if order == "pad thai":
    protein = input("Chicken or tofu? ")

print("You ordered: " + order + " with " + protein + ".")

age = int(input("How old are you? "))    
bus_fare = 4.75
fare_type = "Adults"

#kids under 5 ride for free
if age < 5:
    bus_fare = 0
    fare_type = "Kids"

#Seniors get a dollar off.
if age >= 60:
    bus_fare = bus_fare - 1
    fare_type = "Seniors"

#everyone else pays full price.
print("The " + fare_type + " bus fare is $" + str(bus_fare) + ".")

#Recycling or Trash program
material = input("What material is it? ")
length = float(input("What is its length in cm? "))

if material == "plastic" and length >= 7.5:
    waste_type = "recycling"
else:
    waste_type = "trash"

print("Please deposit your item in the " + waste_type + " bin.")


word_count = 14
sentiment = "neutral"
acount_age_in_days = 2

is_suspicious_length = word_count <= 3 or word_count > 200
is_useful_post = not is_suspicious_length and sentiment != "negative"
is_trusted_user = acount_age_in_days >= 30

#Promote useful posts by trustted users
if is_useful_post and is_trusted_user:
    print("This post has been featured on the hotlist!")

#Spammers tent to use brand new accounts.
if sentiment == "negative" and acount_age_in_days < 7:
    print("This post has been flagged as potential spam.")