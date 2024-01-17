class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        symbols = {"+", "-", "/", "*"}
        n = len(tokens)
        ans = []
        for i in range(n):
            if tokens[i] in symbols:
                b = ans.pop()
                a = ans.pop()
                if tokens[i]=="+":
                    ans.append(a+b)
                elif tokens[i]=="-":
                    ans.append(a-b)
                elif tokens[i]=="*":
                    ans.append(a*b)
                elif tokens[i]=="/":
                    ans.append(int(a/b))
                continue
            ans.append(int(tokens[i]))
        return ans[0]
