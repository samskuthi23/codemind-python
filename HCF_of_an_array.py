a=int(input())
arr=list(map(int,input().strip().split()))
m=100000
for i in range(a):
    if(m>arr[i]):
        m=arr[i]
for i in range(1,m+1):
    c=0
    for j in range(0,a):
        if(arr[j]%i==0):
            c+=1
    if(c==a):
        hcf=i
print(hcf)