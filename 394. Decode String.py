class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        p = ''
        for c in s:
            if c!="]":
                stack.append(c)
            else:
                p = t = n = ''
                
                while True:
                    p = stack.pop()
                    if p=="[":
                        break
                    t = p + t
                
                while stack:
                    p = stack.pop()
                    if p.isalpha() or p=="[":
                        break
                    n = p + n
                
                if p.isalpha() or p=="[":
                    stack.append(p)
                    
                stack.append(int(n)*t)
        
        return ''.join(stack)