class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        arr_e = []
        arr_o = []
        for i in nums:
            if i%2:
                arr_o.append(i)
            else:
                arr_e.append(i)
        return sorted(arr_e)+sorted(arr_o)