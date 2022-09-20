r,c=map(int,input().split())
math=[]
for i in range(r):
    l=list(map(int,input().split()))[:c]
    math.append(l)
ers=0
ors=0
for i in range(r):
    if i%2==0:
        ers=ers+sum(math[i])
    else:
        ors=ors+sum(math[i])
print(ers,ors)
