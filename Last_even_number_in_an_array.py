n=int(input())
a=list(map(int,input().split()))
c=0
#print(*a)
for i in reversed(range(len(a))):
    if a[i]%2==0:
        c=a[i]
        break
print(c)
