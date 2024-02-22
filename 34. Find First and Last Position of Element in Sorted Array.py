class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # Community solution
        def search(arr,t):
            low, high = 0, len(arr)
            while low<high:
                mid = (low+high)//2
                if arr[mid]<t:
                    low = mid+1
                else:
                    high = mid
            return low
        low = search(nums, target)
        high = search(nums, target+1)-1
        if low<=high:
            return [low, high]
        return [-1,-1]

        # My solution
        # try:
        #     return [nums.index(target),len(nums)-nums[::-1].index(target)-1]
        # except:
        #     return [-1,-1]