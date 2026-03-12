n = 4

for i in range(1, n+1):

    # increasing numbers
    for j in range(1, i+1):
        print(j, end=" ")

    # spaces
    for j in range(1, 2*(n-i)+1):
        print(" ", end=" ")

    # decreasing numbers
    for j in range(i, 0, -1):
        print(j, end=" ")

    print()