ag1 = int(input("Enter age :"))
tkPrice1 = float(input("Enter the Ticket Price of First Person :"))
totalPrice = 0

if ag1 < 12:
    totalPrice = totalPrice + (tkPrice1 * 0.30)
elif ag1 > 59:
    totalPrice = totalPrice + (tkPrice1 * 0.50)
else:
    totalPrice = totalPrice + tkPrice1
# person 1 ends here

ag2 = int(input("Enter age :"))
tkPrice2 = float(input("Enter the Ticket Price of Second Person :"))
if ag2 < 12:
    totalPrice = totalPrice + (tkPrice2 * 0.30)
elif ag2 > 59:
    totalPrice = totalPrice + (tkPrice2 * 0.50)
else:
    totalPrice = totalPrice + tkPrice2
# person 2 ends here

ag3 = int(input("Enter age :"))
tkPrice3 = float(input("Enter the Ticket Price of Third Person :"))
if ag3 < 12:
    totalPrice = totalPrice + (tkPrice3 * 0.30)
elif ag3 > 59:
    totalPrice = totalPrice + (tkPrice3 * 0.50)
else:
    totalPrice = totalPrice + tkPrice3
# person 3 ends here

ag4 = int(input("Enter age :"))
tkPrice4 = float(input("Enter the Ticket Price of Forth Person :"))
if ag4 < 12:
    totalPrice = totalPrice + (tkPrice4 * 0.30)
elif ag4 > 59:
    totalPrice = totalPrice + (tkPrice4 * 0.50)
else:
    totalPrice = totalPrice + tkPrice4
# person 4 ends here

ag5 = int(input("Enter age :"))
tkPrice5 = float(input("Enter the Ticket Price of Fifth Person :"))
if ag5 < 12:
    totalPrice = totalPrice + (tkPrice5 * 0.30)
elif ag5 > 59:
    totalPrice = totalPrice + (tkPrice5 * 0.50)
else:
    totalPrice = totalPrice + tkPrice5
# person 5 ends here

print(f"Total price to pay for the trip of Five people is {totalPrice}")