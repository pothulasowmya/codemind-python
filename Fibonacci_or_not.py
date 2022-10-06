n=int(input())
a=1
b=1
c=0
if n==0 or n==1:
    print("True")
else:
    while c<n:
        c=a+b;
        b=a
        a=c
    if c==n:
        print("True")
    else:
        print("False")