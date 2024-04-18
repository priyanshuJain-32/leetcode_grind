class Trie:

    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:
        curr = self.trie
        for w in word:
            if w not in curr:
                curr[w] = {}
            curr = curr[w]
        curr['*'] = ''
        
    def search(self, word: str) -> bool:
        curr = self.trie
        for w in word:
            if w not in curr:
                return False
            curr = curr[w]
        return '*' in curr

    def startsWith(self, prefix: str) -> bool:
        curr = self.trie
        for w in prefix:
            if w not in curr:
                return False
            curr = curr[w]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)