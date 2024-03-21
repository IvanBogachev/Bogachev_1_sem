class Fenwicktree:
    def __init__(self, data: list):
        self.data = data
        self.fen = []
        self.calc_fen()


    def calc_fen(self) -> None:
        for i in range(0, len(self.data)):
            if i == f(i):
                self.fen.append(self.data[i])

            else:
                sum = self.data[i]
                k = i - 1
                while f(i) != f(k):
                    deg = 0
                    sum += self.fen[k]

                    k = f(k) - 1
                    deg += 1

                self.fen.append(self.fen[k] + sum)


def f (i):
    return i&(i+1)
def g (i):
    return i|(i+1)

def fullsum(fen,data, val: int):
    if val == 0:
        return fen[0]
    sum = data[val]
    k = val - 1
    while 0 != f(k):
        deg = 0
        sum += fen[k]
        k = f(k) - 1
        deg += 1
    sum = sum + fen[k]
    return sum


def find_sum(fen, r:int, l:int):
    r_sum = fullsum(fen.fen, fen.data, r) - fen.data[r]
    l_sum = fullsum(fen.fen, fen.data, l)
    return l_sum - r_sum

def update(fen, pos, val):
    while pos < len(fen.data):
        fen.fen[pos] += val
        pos = g(pos)
    return fen.fen






fen1 = Fenwicktree([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32])
print(fen1.fen)

print(find_sum(fen1,2,8))
print(update(fen1,0,10))