n=int(input())
l=list(map(int,input().split()))
e=0
for i in range(n):
    if i%2==0:
        e=e+l[i]
print(e)