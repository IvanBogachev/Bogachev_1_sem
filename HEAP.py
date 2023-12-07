class Heap:
    numbers = []


    def add(self, element):
        self.numbers.append(element)

    def show(self):
        return self.numbers

    def heap_element(self, i, n):
        i_left = 2 * i + 1
        i_right = 2 * i + 2
        i_largest = i

        if i_left <= n and self.numbers[i_left] > self.numbers[i_largest]:
            i_largest = i_left
        if i_right <= n and self.numbers[i_right] > self.numbers[i_largest]:
            i_largest = i_right

        if i_largest == i:
            return
        else:
            self.numbers[i_largest], self.numbers[i] = self.numbers[i], self.numbers[i_largest]
            self.heap_element(i_largest, n)

    def build_max_heap(self):
        i_middle = len(self.numbers) // 2
        for id in reversed(range(0, i_middle + 1)):

            self.heap_element(id, len(self.numbers) - 1)

    def heap_min(self):
        self.build_max_heap()
        for id in reversed(range(0, len(self.numbers))):
            self.numbers[0], self.numbers[id] = self.numbers[id], self.numbers[0]
            self.heap_element(0, id - 1)
        return self.numbers

    def heap_max(self):
        self.heap_min()
        for id in reversed(range(0, len(self.numbers) // 2)):
            self.numbers[len(self.numbers) - 1 - id], self.numbers[id] = self.numbers[id], self.numbers[len(self.numbers) - 1 - id]
        return self.numbers

    def delete(self, index):
        del self.numbers[index]

    def get_child(self, index):
        left_child = None
        right_child = None
        i_left_child = 2 * index + 1
        i_right_child = 2 * index + 2
        if i_right_child < len(self.numbers):
            right_child = self.numbers[i_right_child]
        if i_left_child < len(self.numbers):
            left_child = self.numbers[i_left_child]
        return left_child, right_child



heap = Heap()

heap.add(1)
heap.add(3)
heap.add(9)
heap.add(23)
heap.add(11)
heap.add(4)
heap.heap_min()



print(heap.heap_min())

print(heap.get_child(2))