A = list(input().split())
B = 0
C = 0
D = 0
for i in range(len(A)):
    B = A.count(A[i])
    if B > C:
        C = B
for i in range(len(A)):
    B = A.count(A[i])
    if B == C:
        D=A[i]
print(D)
