A = list(input().split())
a = int(A[0])
b = A[1]
c = int(len(b)/a)
d = []
p = 0
q = 1
z=str()
for i in range(a):
    d.append(b[c*p:c*q])
    p+=1
    q+=1
for i in range(a):
    d[i]=d[i][::-1]
for i in range(a):
    z+=d[i]
print(z)