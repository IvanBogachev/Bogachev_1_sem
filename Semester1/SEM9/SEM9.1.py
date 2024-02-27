a = list(input().split())
c = []
for i in range(len(a)):
    if a[i] == "*":
        x1 = c.pop()
        x2 = c.pop()
        c.append(int(x2) * int(x1))
    elif a[i] == "-":
        x1 = c.pop()
        x2 = c.pop()
        c.append(int(x2) - int(x1))
    elif a[i] == "+":
        x1 = c.pop()
        x2 = c.pop()
        c.append(int(x2) + int(x1))
    elif a[i] == "/":
        x1 = c.pop()
        x2 = c.pop()
        c.append(int(x2) / int(x1))
    else:
        c.append(a[i])
print(c[0])