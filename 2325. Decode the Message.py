class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        d = {" ": " "}
        alpha = "abcdefghijklmnopqrstuvwxyz"
        k = 0
        for i in key:
            try:
                d[i]
            except:
                d[i] = alpha[k]
                k+=1
        ans = ""
        for i in message:
            ans += d[i]
        return ans