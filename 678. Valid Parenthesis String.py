class Solution:
    def checkValidString(self, s: str) -> bool:
        stack_p, stack_s, stack_c = [], [], []
        i = 0

        while i<len(s):
            if s[i]=="(":
                stack_p.append(i)

            elif s[i]=="*":
                stack_s.append(i)

            else:
                if stack_p:
                    stack_p.pop()
                else:
                    stack_c.append(i)
            i+=1
        
        # Remove the open braces with the stars
        i,j = 0,0
        len_stack_p = len(stack_p)
        
        while i<len_stack_p and j<len(stack_s):
            if not stack_s:
                return False
            if stack_p[i]<stack_s[j]:
                stack_s.pop(j)
                i+=1
            else:
                j+=1
        
        # Remove the close braces with the stars
        k, j = 0, 0
        len_stack_c = len(stack_c)
        while k<len_stack_c and j<len(stack_s):
            if not stack_s:
                return False
            if stack_c[k]>stack_s[j]:
                k+=1
                stack_s.pop(j)
            else:
                return False
        
        # Check if both stacks reached the end
        return i==len_stack_p and k==len_stack_c