x = int(input("Enter x: "))
n = int(input("Enter Number of Terms: "))

sum = 0
sign = 1
denominator = 1

for i in range(1, n + 1):

    sum = sum + sign * (x ** i) / denominator

    sign = sign * -1
    denominator = denominator + 2

print("Sum =", sum)