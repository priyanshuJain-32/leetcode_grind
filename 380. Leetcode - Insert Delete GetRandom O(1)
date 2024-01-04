class RandomizedSet:

    def __init__(self):
        self.dict = {}
        self.arr = []

    def insert(self, val: int) -> bool:
        try: 
            if self.dict[val]:
                return False
        except:
            self.arr.append(val)
            self.dict[val] = len(self.arr)-1
            return True

    def remove(self, val: int) -> bool:
        try: 
            if int(self.dict[val])==self.dict[val]:
                remove_i = self.dict[val]
                self.arr[remove_i] = self.arr[-1]
                self.dict[self.arr[remove_i]] = remove_i
                self.dict.pop(val)
                self.arr.pop()
                return True
        except:
            return False

    def getRandom(self) -> int:
        return random.choice(self.arr)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
