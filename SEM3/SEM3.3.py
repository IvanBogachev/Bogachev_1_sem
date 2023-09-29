def opop(A):
    x = -9
    while ((d-x*A[0])/A[1])%1 != 0:
        x+=1
    return x, int(((d-x*A[0])/A[1]))
A = list(map(int,input().split()))
b=A[0]
c=A[1]

while b != 0 and c != 0:
    if b > c:
        b = b%c
    else:
        c = c%b
d = c+b
print(*list(opop(A)),d)


