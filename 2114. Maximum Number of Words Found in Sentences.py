class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        maxi = 0
        for i in sentences:
            maxi = max(maxi, len(i.split()))
        return maxi