A = list(input().split())
B = 0
for i in range(len(A)):
    B = A.count(A[i])
    if B == 1:
        print(A[i])