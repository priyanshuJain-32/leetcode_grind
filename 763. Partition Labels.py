class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ans = [0]
        i = 0
        start = s[0]
        n = len(s)
        max_r = n - s[::-1].index(start)-1
        
        while max_r<n:
            seen = set()
            while i<=max_r:
                if s[i] not in seen:
                    max_r = max(max_r, n-1-s[::-1].index(s[i]))
                    seen.add(s[i])
                i += 1
            ans.append(i-sum(ans))
            if i<n:
                max_r = n-1-s[::-1].index(s[i])
            else:
                break
        return ans[1:]