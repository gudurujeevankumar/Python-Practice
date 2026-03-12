num=int(input())
new=num
count=0
sum=0
n=num
while num!=0:
    digit =num%10
    count+=1
    num//=10
while new!=0:
    digit=new%10
    sum+=digit**count
    new//=10
if sum==n:
    print(True)
else:
    print(False)

