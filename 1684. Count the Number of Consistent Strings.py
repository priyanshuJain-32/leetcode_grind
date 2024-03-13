class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        a = set(allowed)
        cnt = 0
        for i in words:
            if len(set(i)-a)==0:
                cnt += 1
        return cnt