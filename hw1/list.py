class Node:
    def __init__(self, key, val):
        self.prev = None
        self.next = None
        self.val = val
        self.key = key
    
    def __str__(self):
        return f"{self.key} : {self.val}"

class List:
    def __init__(self):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.size = 0
        self.head.next = self.tail
        self.tail.prev = self.head

    def append(self, key, val):
        node = Node(key, val)
    
        p = self.tail.prev
        p.next = node
        self.tail.prev = node
        node.prev = p
        node.next = self.tail
        
        self.size += 1
        return node

    def pop(self):
        return self.remove(self.head.next)

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1
        return node
