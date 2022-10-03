def amount(n,t,k):
    s=0
    for i in range(n):
        if k[i]>t:
            s+=2
        else:
            s+=1
    return s
k=[]
n=int(input())
for i in range(n):
    m=int(input())
    k.append(m)
t=int(input())
print(amount(n,t,k))