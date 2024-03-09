class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        def prime(n):
            if n<2:
                return False
            if n==2 or n==3:
                return True
            sqrt = int(math.sqrt(n))
            for i in range(2,sqrt+1):
                if n%i==0:
                    return False
            return True
        max_prime = 0
        dim = len(nums)
        for i in range(dim):
            for j in range(dim):
                if i==j:
                    if prime(nums[i][j]):
                        max_prime = max(max_prime, nums[i][j])
                elif i+j==dim-1:
                    if prime(nums[i][j]):
                        max_prime = max(max_prime, nums[i][j])
        return max_prime