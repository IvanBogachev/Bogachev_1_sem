def polish_result(b):
    a = list(b.split())
    c = []
    for i in range(len(a)):
        if a[i] == "*":
            if len(c) < 2:
                return "выражение составлено некорректно"
            else:
                x1 = c.pop()
                x2 = c.pop()
                c.append(int(x2) * int(x1))
        elif a[i] == "-":
            if len(c) < 2:
                return "выражение составлено некорректно"
            else:
                x1 = c.pop()
                x2 = c.pop()
                c.append(int(x2) - int(x1))
        elif a[i] == "+":
            if len(c) < 2:
                return "выражение составлено некорректно"
            else:
                x1 = c.pop()
                x2 = c.pop()
                c.append(int(x2) + int(x1))
        elif a[i] == "/":
            if len(c) < 2:
                return "выражение составлено некорректно"
            else:
                x1 = c.pop()
                x2 = c.pop()
                c.append(int(x2) / int(x1))
        else:
            c.append(a[i])
    if len(c) != 1:
        return "выражение составлено некорректно"
    else:
        return c[0]


print(polish_result(input()))