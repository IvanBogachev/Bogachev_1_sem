A = list(input().split())
B = str()
if len(A)%2 == 0:
    for i in range(0, len(A) - 1, 2):
        B += A[i + 1]
        B += A[i]
    print(B)

else:
    for i in range(0, len(A) - 1, 2):
        B += A[i + 1]
        B += A[i]
    B += A[len(A)-1]
    print(B)