from list import List

class LRUCache:
    def __init__(self, capacity: int=10):
        self.size = capacity
        self.list = List()
        self.h = {}

    def get(self, key: str) -> str:
        if key in self.h:
            node = self.h[key]
            self.list.remove(node)
            self.h[key] = self.list.append(key, node.val)
            return node.val
        return None

    def set(self, key: str, value: str) -> None:
        if key in self.h:
            self.list.remove(self.h[key])

        node = self.list.append(key, value)
        self.h[key] = node

        if self.list.size > self.size:
            d = self.list.pop()
            del self.h[d.key]
            
    def rem(self, key: str) -> None:
        node = self.h[key]
        self.list.remove(node)
        del self.h[key]

    def __len__(self) -> int:
        # print(self.h.keys())
        return len(self.h)