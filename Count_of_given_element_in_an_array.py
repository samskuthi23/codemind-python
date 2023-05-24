n=int(input())
l=list(map(int,input().split()))
k=int(input())
c=0
for i in range(n):
    if l[i]==k:
        c+=1
print(c)
