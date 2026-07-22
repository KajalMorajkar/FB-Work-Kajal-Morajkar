start = int (input("Enter number :"))
endvr = int(input ("Enter number :"))
d = int (input ("Enter divisor:"))
for i in range (start, endvr+1):
    if (i % d ==0):
        print(i)