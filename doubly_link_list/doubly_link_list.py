class DoublyLinkedList(object):
    def __init__(self, value):

        self.value = value
        self.next_node = None
        self.prev_node = None


a = DoublyLinkedList(1)
b = DoublyLinkedList(2)
c = DoublyLinkedList(3)

a.next_node = b
b.prev_node = a

b.next_node = c
c.prev_node = b

print(a.value)  # 1
print(a.next_node.value)  # 2
print(b.value)  # 2
print(b.prev_node.value)  # 1
print(b.next_node.value)  # 3
