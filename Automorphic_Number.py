n=int(input())
s=n*n
while n:
    r=n%10
    k=s%10
    if r!=k:
       print("Not an Automorphic Number")
       break
    else:
       n=n//10
       s=s//10
else:
    print("Automorphic Number")