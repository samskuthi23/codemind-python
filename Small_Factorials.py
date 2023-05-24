n = int(input())
while n:
    n-=1
    x=int(input())
    fact=1
    while x!=1:
        fact*=x
        x-=1
    print(fact)