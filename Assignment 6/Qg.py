rows = 5

for i in range(1, rows+1):

    for j in range(rows-i):
        print("  ", end="")

    ch = 65

    for j in range(2*i-1):
        print(chr(ch), end=" ")
        ch = ch + 1

    print()