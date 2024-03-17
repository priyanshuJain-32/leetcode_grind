class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        seen = set()
        count = 0
        for i in sentence:
            if i not in seen:
                seen.add(i)
                count += 1
            elif count==26:
                return True
        return count==26