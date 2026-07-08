cost = float(input("Enter Cost Price: "))
discount = float(input("Enter Discount (%): "))

selling = cost - (cost * discount / 100)

print("Selling Price =", selling)