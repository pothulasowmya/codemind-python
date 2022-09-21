n=int(input())
while True:
    sum=rem=0
    if n>=0 and n<=9:
        if n==1 or n==7:
            print(True)
            break
        else:
            print(False)
            break
    else:
        while n:
            rem=n%10
            sum+=rem*rem
            n=n//10
        n=sum