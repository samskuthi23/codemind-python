x = int(input())
c=0
for i in range(1,x//2):
    if i*(i+1)==x:
        print('YES')
        c=1
if c==0:
    print('NO')