class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        n = len(words)
        ans = []
        for ch in words[0]:
            flag = True
            for i in range(1,n):
                if ch not in words[i]:
                    flag = False
                    break
                words[i] = words[i].replace(ch,"",1)
            if flag: ans.append(ch)
                
        return ans