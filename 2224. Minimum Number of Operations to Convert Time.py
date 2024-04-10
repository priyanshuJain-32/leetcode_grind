class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        cuh, cum = list(map(int,current.split(":")))
        coh, com = list(map(int,correct.split(":")))
        
        self.ops = coh-cuh
        self.mdiff = com-cum

        if self.mdiff <0:
            self.mdiff = 60-abs(self.mdiff)
            self.ops -= 1
        
        def incrementops(t):
            while self.mdiff>=t:
                self.ops += 1
                self.mdiff -= t
        
        incrementops(15)
        
        incrementops(5)
        
        incrementops(1)
        
        return self.ops