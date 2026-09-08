n = int(input("Enter Number: "))

sum = 0
fact = 1

for i in range(1, n + 1):
    fact = fact * i
    sum = sum + fact

print("Sum =", sum)