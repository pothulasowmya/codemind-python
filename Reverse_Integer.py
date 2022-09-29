a=int(input())    
n=abs(a)
rev=0
while n:
    rem=n%10
    rev=rev*10+rem
    n=n//10
if a>10:
    print(rev)
else:
    print('-',rev,sep='')
