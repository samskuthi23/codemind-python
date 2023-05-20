l=list(map(int,input().split(',')))
k=0
s=[]
c=0
for i in l:
    k=0
    for j in range(1,i+1):
        if(i%j==0):
            k=k+j
    if k in l:
        s.append(i)
        c+=1
if(c==0):
    print("-1")
else:
    s=sorted(s)
    print(*s)