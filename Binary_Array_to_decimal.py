k=int(input())
s=list(map(int,input().split()))
for i in range(len(s)):
    s[i]=str(s[i])
a="".join(s)
print(int(a,2))