si = 65
n = int(input("Enter number of rows : "))
for i in range(1, n+1):
    for j in range(i):
        print(chr(si),end=" ")
        si += 1
    print()