a=int(input())
b=int(input())
c=0
d=0
for i in range(1,a):
    if a%i==0:
        c=c+i
for j in range(1,b):
    if b%j==0:
        d=d+j
if a==d and b==c:
    print("Amicable")
else:
    print("Not Amicable")
    
        