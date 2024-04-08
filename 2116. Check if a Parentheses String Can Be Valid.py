class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s)%2==1:
            return False
        
        unlocked = []
        stack_open = deque()
        
        delta = 0
        for i,(p,l) in enumerate(zip(s,locked)):
            if l=="1":
                if p=="(":
                    stack_open.append(i)
                    delta += 1
                else:
                    if stack_open:
                        stack_open.pop()
                    delta -=1
                    if delta<0:
                        try: 
                            unlocked.pop()
                            delta+=1
                        except: return False
            else:
                unlocked.append(i)
        
        i,j=0,0
        while stack_open and unlocked:
            try:
                if stack_open[i]<unlocked[j]:
                    stack_open.popleft()
                    unlocked.pop(j)
                else:
                    j+=1
            except: return False
        
        return not stack_open and len(unlocked)%2==0