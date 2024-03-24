class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        def helper(s, word, m):
            if s[:m]==word:
                return 1
            return 0
        
        cnt = 0
        for word in words:
            cnt += helper(s, word, len(word))
        return cnt