class Solution:
    def hammingWeight(self, n: int) -> int:
        # 1st Approach
        # count = 0
        # for i in str(bin(n)[2:]):
        #     if i=='1':
        #         count += 1
        # return count

        # Fastest Approach
        return bin(n).count("1")
        
        # 3rd Approach
        # res = 0
        # while str(n)!='0':
        #     res += n&1
        #     n>>=1
        # return res
