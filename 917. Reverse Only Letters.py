class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        i, n = 0, len(s)
        j = n-1
        ans = list(s)
        while i<j:
            if ans[i].isalpha() and ans[j].isalpha():
                ans[i], ans[j] = ans[j], ans[i]
            elif ans[i].isalpha():
                j-=1
                continue
            elif ans[j].isalpha():
                i+=1
                continue
            i+=1
            j-=1
            
        # Another way
        # while j>-1:
        #     curr = ord(s[j])
        #     if 65<=curr<=90 or 97<=curr<=122:
        #         ans.append(s[j])
        #     j-=1
        # while i<n:
        #     curr = ord(s[i])
        #     if not (65<=curr<=90 or 97<=curr<=122):
        #         ans.insert(i,s[i])
        #     i+=1
        return "".join(ans)