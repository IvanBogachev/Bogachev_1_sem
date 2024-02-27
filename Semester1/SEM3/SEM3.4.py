def treugolnik(size,symb):
    for i in range(1,int(size)//2+2):
        w = str(i*symb)
        print(w)
    q = str(symb) * (size // 2 + 1)
    for i in range(1, int(size) // 2+1):
        w = q[:-i*len(symb)]
        print(w)
    return w[:-i*len(symb)]
print(treugolnik(7,"c"))








