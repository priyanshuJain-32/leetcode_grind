class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        ans = 0
        n = len(arr)
        for k in range(1,n+1,2):
            i = 0
            m_ans = sum(arr[:k])
            ans += m_ans
            while i<n-k:
                m_ans -= arr[i]
                m_ans += arr[i+k]
                ans += m_ans
                i+=1
        return ans