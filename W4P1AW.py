#Project 1 Hotel – Quick Cut Falls
# "A Cut Above The Rest."

# Input
def get_input():
    customer_name = input("Enter the customer's first and last name: ")
    first_night = input("Enter the date of the customer's first night (mm/dd/yyyy): ")
    nights_staying = int(input("Enter how many nights the customer will be staying for: "))
    room_price = float(input("Enter the price of the room per night: $"))
    extra_cots = int(input("Enter the number of extra cots the customer wants set up: "))
    early_check_in_fee = float(input("Enter the early check in fee (0 if they are not checking in early): $"))
    gym_fee = float(input("Enter the gym fee: $"))
    aaa_discount = float(input("Enter the AAA discount amount: $"))

    return customer_name, first_night, nights_staying, room_price, extra_cots, early_check_in_fee, gym_fee, aaa_discount

# Process
def process_data(customer_name, first_night, nights_staying, room_price, extra_cots, early_check_in_fee, gym_fee, aaa_discount):
    # Format customer name
    names = customer_name.split()
    formatted_name = f"{names[1].capitalize()}, {names[0].capitalize()}"

    # Extract year and month from first night date
    year = first_night.split('/')[-1]
    month = first_night.split('/')[0]

    # Generate invoice number
    invoice_number = f"{names[1][0].upper()}{names[0][0].upper()}{year}{month.rjust(2, '0')}"

    # Calculate totals
    cots_total = extra_cots * 25.00

    total_charge = nights_staying * room_price + cots_total

    housekeeping_fee = total_charge * 0.10

    total_invoice = total_charge + early_check_in_fee + gym_fee + housekeeping_fee

    amount_owed = total_invoice - aaa_discount

    return formatted_name, invoice_number, nights_staying, room_price, extra_cots, cots_total, total_charge, housekeeping_fee, early_check_in_fee, gym_fee, total_invoice, aaa_discount, amount_owed

# Output
def print_invoice(formatted_name, invoice_number, nights_staying, room_price, extra_cots, cots_total,
                  total_charge, housekeeping_fee, early_check_in_fee, gym_fee, total_invoice,
                  aaa_discount, amount_owed):
    print("\nWapakoneta's Quick Cut Falls")
    print("***A Cut Above The Rest***")
    print(f"Customer: {formatted_name}")
    print(f"Invoice Number: {invoice_number}")
    print(f"Invoice of Nights: {nights_staying}")
    print(f"Price per Night: ${room_price:.2f}")
    print(f"Number of Extra Cots: {extra_cots}")
    print(f"Cots Total: ${cots_total:.2f}")
    print(f"Total Charge: ${total_charge:.2f}")
    print(f"Housekeeping Fee: ${housekeeping_fee:.2f}")
    print(f"Early Check In Fee: ${early_check_in_fee:.2f}")
    print(f"Gym Fee: ${gym_fee:.2f}")
    print(f"Total Invoice: ${total_invoice:.2f}")
    print(f"Triple AAA discount: ${aaa_discount:.2f}")
    print(f"Amount Owed: ${amount_owed:.2f}")

# Main
def main():
    customer_name, first_night, nights_staying, room_price, extra_cots, early_check_in_fee, gym_fee, aaa_discount = get_input()
    formatted_name, invoice_number, nights_staying, room_price, extra_cots, cots_total, total_charge, housekeeping_fee, early_check_in_fee, gym_fee, total_invoice, aaa_discount,amount_owed = process_data(customer_name, first_night, nights_staying, room_price, extra_cots, early_check_in_fee, gym_fee, aaa_discount)
    print_invoice(formatted_name, invoice_number, nights_staying, room_price, extra_cots, cots_total, total_charge, housekeeping_fee, early_check_in_fee, gym_fee, total_invoice, aaa_discount, amount_owed)

# Call main function
main()