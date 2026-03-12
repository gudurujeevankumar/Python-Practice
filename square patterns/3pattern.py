n = 4
count = 0
for i in range(n):
    for j in range(1,n+1):
        count = count + 1
        print(count, end=" ")
        if count==9 : count = 0
    print()