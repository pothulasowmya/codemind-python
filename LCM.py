a,b=map(int,input().split())
for i in range(1,b+1):
    if(b*i)%a==0:
      print(b*i)
      break
else:
    if(a*i)%b==0:
      print*(a*i)