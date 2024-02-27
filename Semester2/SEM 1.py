import numpy as np

class SumTree:

    def __init__(self, data: list):
        ln = len(data)
        lb = np.log2(ln)
        if lb == int(lb):
            self.data = data
        else:
            self.data = data
            lb = int(lb) + 1
            for i in range(ln, 2 ** lb):
                self.data.append(0)

        self.tree = [0 for i in range(len(self.data) - 1)] + self.data
        self.calc_tree()

    def calc_tree(self) -> None:
        for i in range(len(self.tree) + 1, 2, -2):
            s1 = self.tree[i - 2]
            s2 = self.tree[i - 3]
            sm = s1 + s2
            self.tree[(i - 4) // 2] = sm

def Sum(tree, l: int, r: int):
        def tree_sum(l: int, r: int, tl=0, tr=len(tree.data) - 1):
            sum = 0

            tm = (tl + tr + 1) // 2
            if tr == tl:
                return tree.data[tm]

            if l <= tl and r >= tr:

                index1 = (len(tree.data) - 1) + tr  # 14
                index2 = (len(tree.data) - 1) + tl + 1  # 8

                while index1 != index2:
                    index1 = max((index1 - 2) // 2, 0)  # 6
                    index2 = max((index2 - 1) // 2, 0)  # 3
                if tl + 1 == tr:
                    return tree.tree[(index1 - 2) // 2]
                else:
                    return tree.tree[index1]

            go_left = l < tm
            go_right = r >= tm

            if go_left:
                sum += tree_sum(l, r, tl=tl, tr=tm - 1)
            if go_right:
                sum += tree_sum(l, r, tl=tm, tr=tr)

            return sum

        return tree_sum(l, r)



def Update(tree, id: int, value: int):
    tree.tree[id + len(tree.data) - 1] = value

    if id % 2 == 1:
            s1 = tree.tree[id + len(tree.data) - 2]
            s2 = value
            sm = s1 + s2
            tree.tree[(id + len(tree.data) - 2) // 2] = sm
            id = (id + len(tree.data) - 2) // 2

    else:
            s1 = value
            s2 = tree.tree[id + len(tree.data)]
            sm = s1 + s2
            tree.tree[(id + len(tree.data) - 1) // 2] = sm
            id = (id + len(tree.data) - 1) // 2


    for i in range(int(np.log2(len(tree.data))) - 1):
        if id % 2 == 0:
            s1 = tree.tree[id - 1]
            s2 = tree.tree[id]
            sm = s1 + s2
            tree.tree[(id - 2) // 2] = sm
            id = (id - 2) // 2

        else:
            s1 = tree.tree[id]
            s2 = tree.tree[id + 1]
            sm = s1 + s2
            tree.tree[(id - 1) // 2] = sm
            id = (id - 1) // 2
    return tree.tree

tree = SumTree([1,2,3,4,5,6,7,8])

print(tree.tree)

Update(tree,0,99)

print(tree.tree)

Update(tree,5,64)

print(tree.tree)



print(Sum(tree,0,6))

