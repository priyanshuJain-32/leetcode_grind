class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_diff = 3000000
        min_arr = []
        for i in range(len(arr)-1):
            d = arr[i+1]-arr[i]
            if d>min_diff:
                continue
            elif d<min_diff:
                min_diff = d
                min_arr = []
            min_arr.append([arr[i],arr[i+1]])
        return min_arr