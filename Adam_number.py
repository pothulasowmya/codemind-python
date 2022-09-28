n=int(input())
sq=n*n
rev=0
rev2=0
while n>0:
  r=n%10
  rev=rev*10+r
  n=n//10
  s=rev**2
while s>0:
   r2=s%10
   rev2=rev2*10+r2
   s=s//10
if sq==rev2:
    print("True")
else:
    print("False")


