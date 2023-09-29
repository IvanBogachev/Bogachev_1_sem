def prostoe(n):
    p = str(n)
    for i in range(1,len(p)+1):
        print(n%10,"*",10**(i-1))
        n = n//10

n = int(input())
print(prostoe(n))