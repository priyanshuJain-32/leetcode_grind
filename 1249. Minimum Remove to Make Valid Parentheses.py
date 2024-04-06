class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack_o = []
        s = list(s)
        i, delta = 0, 0
        while i<len(s):
            if s[i]=="(":
                stack_o.append(i)
                delta+=1
            elif s[i]==")":
                if stack_o:
                    stack_o.pop()
                delta-=1
            if delta<0:
                s[i]=""
                delta+=1
            i+=1
        
        j = len(stack_o)-1
        while delta>0:
            s[stack_o[j]]=""
            j-=1
            delta-=1
        return "".join(s)