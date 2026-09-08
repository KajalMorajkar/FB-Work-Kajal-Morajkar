n = int(input("Enter Number of Students: "))

total_percentage = 0

for i in range(n):
    print("\nStudent", i + 1)

    total = 0

    for j in range(5):
        marks = int(input("Enter Subject Marks: "))
        total = total + marks

    percentage = total / 5
    print("Percentage =", percentage)

    total_percentage = total_percentage + percentage

average = total_percentage / n
print("\nAverage Percentage =", average)