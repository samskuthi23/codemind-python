n=int(input())
x=list(map(int,input().split()))
a,b=map(int,input().split())
s=sum(x)
d=0
for i in x:
    if i>=a and i<=b:
        d+=i
print(s-d)        
