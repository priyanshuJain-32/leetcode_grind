class MyHashMap:

    def __init__(self):
        self.hashmap = defaultdict(lambda: -1)

    def put(self, key: int, value: int) -> None:
        self.hashmap[key] = value

    def get(self, key: int) -> int:
        return self.hashmap[key]

    def remove(self, key: int) -> None:
        if key in self.hashmap:
            del self.hashmap[key]


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)