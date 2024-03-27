class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rows = [{'q','w','e','r','t','y','u','i','o','p'}, {'a','s','d','f','g','h','j','k','l'}, {'z','x','c','v','b','n','m'}]
        ans = []
        for word in words:
            wordl = word.lower()
            for row in rows:
                flag = True
                for ch in wordl:
                    if ch not in row:
                        flag = False
                        break
                if flag:
                    ans.append(word)
                    break
        return ans