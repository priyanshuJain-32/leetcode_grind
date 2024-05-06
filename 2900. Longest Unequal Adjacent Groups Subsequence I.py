class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        i,j = 0,1
        pick = [words[0]]
        while j<len(words):
            if groups[i]!=groups[j]:
                pick.append(words[j])
                i = j
                j += 1
            else:
                j += 1
        return pick