class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        ret = []
        for i,word in enumerate(words):
            if x in word:
                ret.append(i)
        return ret