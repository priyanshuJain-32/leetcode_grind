# import random
class Solution:

    def __init__(self, m: int, n: int):
        self.m, self.n = m, n
        self.dim = m*n
        self.r = random.Random()
        self.flipped = set()

    def flip(self) -> List[int]:
        pos = self.r.randint(0,self.dim-1)
        while pos in self.flipped:
            pos = self.r.randint(0,self.dim-1)
        self.flipped.add(pos)
        i, j = pos//self.n, pos%self.n
        return [i,j]
        
    
    def reset(self) -> None:
        self.flipped = set()
        # self.indices = random.sample(self.indices,self.dim)


# Your Solution object will be instantiated and called as such:
# obj = Solution(m, n)
# param_1 = obj.flip()
# obj.reset()