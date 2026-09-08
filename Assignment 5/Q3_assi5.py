passengers = int(input("Enter Number of Passengers: "))
ticket = int(input("Enter Ticket Cost: "))

total = 0

for i in range(passengers):
    age = int(input("Enter Age: "))

    if age < 12:
        amount = ticket * 70 / 100
    elif age > 59:
        amount = ticket * 50 / 100
    else:
        amount = ticket

    total = total + amount

print("Total Ticket Amount =", total)