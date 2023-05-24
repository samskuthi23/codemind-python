n=int(input())
s=list(map(int,input().split()))
a=sum(s)
c=a//n
h=0
for i in range(n):
    if(s[i]<=c):
        h+=1
print(h)
