A = list(map(int, input().split()))
b=0
c=0
for i in range(A[0]):
    b+=A[i]
d= b - A[0]
for i in range(A[0]+1):
    c=c+i
print(c-d)