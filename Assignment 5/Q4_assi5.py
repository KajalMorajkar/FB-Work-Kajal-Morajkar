start = int(input("Enter Start: "))
end = int(input("Enter End: "))

for num in range(start, end + 1):
    temp = num
    digits = len(str(num))
    sum = 0

    while temp > 0:
        rem = temp % 10
        sum = sum + rem ** digits
        temp = temp // 10

    if sum == num:
        print(num)