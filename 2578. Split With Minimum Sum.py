class Solution:
    def splitNum(self, num: int) -> int:
        num = sorted(str(num))
        Nums = ['','']
        for i in range(0,len(num),2):
            Nums[0] += num[i]
            try:
                Nums[1] += num[i+1]
            except:
                break
        return int(Nums[0])+int(Nums[1])