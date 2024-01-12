class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seq = defaultdict(list)
        visited = defaultdict(bool)
        seq_len = 0
        for i in nums:
            if visited[i]:
                continue
            visited[i] = True
            left, right = i, i
            if seq[i+1]:
                right = seq[i+1][1]
            if seq[i-1]:
                left = seq[i-1][0]
            seq[right] = [left, right]
            seq[left] = [left, right]
            seq_len = max(seq_len, right-left + 1)
        return seq_len
