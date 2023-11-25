class DLinkedList:
    head = None
    tail = None
    lenght = 0
    class Node:
        element = None
        next_node = None
        previous_node = None

        def __init__(self, element, next_node=None, previous_node=None):
            self.element = element
            self.next_node = next_node
            self.previous_node = previous_node

    def append(self, element):
        self.lenght += 1
        if not self.head:
            self.head = self.Node(element)
            return element

        node = self.head
        while node.next_node:
            node = node.next_node

        node.next_node = self.Node(element, previous_node = node)
        self.tail = self.Node(element, previous_node = node)

    def inset(self, element, index):
        self.lenght += 1
        i = 0
        node = self.head
        prev_node = self.head
        while i < index:
            prev_node = node
            node = node.next_node
            i += 1
        prev_node.next_node = self.Node(element, next_node = node, previous_node = prev_node)
        return element

    def delete(self, index):
        if index == 0:
            node = self.head
            element = node.element
            self.head = self.head.next_node
            self.head.previous_node = None
            del node
            return element

        if index == self.lenght - 1:
            node = self.head
            element = node.element
            self.tail = self.tail.previous_node
            self.tail.next_node = None
            del node
            return element


        node = self.head
        prev_node = node
        next_node = node.next_node
        i = 0
        while i < index:
            prev_node = node
            node = node.next_node
            next_node = node.next_node
            i += 1

        prev_node.next_node = node.next_node
        next_node.prev_node = node.previous_node
        element = node.element
        del node
        return element

    def out(self):
        node = self.head
        while node.next_node:
            print(node.element)
            node = node.next_node
        print(node.element)

    def contains(self, element):
        node = self.head
        while node.next_node:
            if element == node.element:
                return True
            else:
                node = node.next_node
        return False

    def get(self, index):
        i = 0
        node = self.head
        while i < index:
            node = node.next_node
            i += 1
        return node.element


dlinked_list = DLinkedList()
dlinked_list.append(10)
dlinked_list.append(20)
dlinked_list.append(30)
dlinked_list.append(40)
dlinked_list.append(50)
dlinked_list.append(60)
dlinked_list.delete(2)
dlinked_list.inset("xxx", 3)

dlinked_list.out()
print(f"Длина списка : {dlinked_list.lenght}")