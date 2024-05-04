class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return
        self.ans = dict()
        self.depth = 0
        def travel(root,depth):
            if not root:
                return
            self.ans[depth] = max(self.ans.get(depth,-2**31-1),root.val)
            self.depth = max(self.depth,depth)
            travel(root.left,depth+1)
            travel(root.right,depth+1)
        travel(root,0)
        return [self.ans[i] for i in range(self.depth+1)]