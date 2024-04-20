class WordDictionary:

    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        curr = self.trie
        for w in word:
            if w not in curr:
                curr[w] = {}
            curr = curr[w]
        curr['*'] = {}

    def search(self, word: str) -> bool:
        def dfs(curr,word):
            if not word:
                return '*' in curr
            if word[0]==".":
                for k in curr.keys():
                    if dfs(curr[k],word[1:]):
                        return True
            elif word[0] in curr:
                return dfs(curr[word[0]],word[1:])
            
            return False
        return dfs(self.trie,word)
                    



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)