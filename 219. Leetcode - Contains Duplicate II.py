class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        num_idx = {}
        for v in range(len(nums)):
            if nums[v] not in num_idx:
                num_idx[nums[v]] = v
            else:
                if (v - num_idx[nums[v]] <= k):
                    return True
                num_idx[nums[v]] = v
        return False
