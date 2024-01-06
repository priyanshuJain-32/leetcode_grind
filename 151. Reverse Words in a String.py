class Solution:
    def reverseWords(self, s: str) -> str:
        
        return " ".join((s.strip()).split()[::-1])

        # return " ".join([i for i in s.split(" ")[::-1] if i!=''])
