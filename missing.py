a = [1,2,4,5]

for i in range(len(a)-1):
    if a[i+1] != a[i] + a[0]:
        print(a[i] + a[0])