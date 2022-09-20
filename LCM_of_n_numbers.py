def Lcm(a,b):
    if a>b:
        h=a
        s=b
    else:
        h=b
        s=a
    for i in range(1,h+1):
        if(h*i)%s==0:
            return(h*i)
n=int(input())
j=list(map(int,input().split()))
l=1
for i in j:
    l=Lcm(l,i)
print(l)