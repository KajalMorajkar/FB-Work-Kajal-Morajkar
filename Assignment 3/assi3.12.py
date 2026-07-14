num = int(input("Enter a 3-digit number: "))

if num >= 100 and num <= 999:
    first = num // 100
    last = num % 10

    if first == last:
        print("The number is a Palindrome.")
    else:
        print("The number is not a Palindrome.")
else:
    print("Please enter a valid 3-digit number.")