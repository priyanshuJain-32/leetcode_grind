class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        self.max_depth, self.ans = 0, [root.val]
        def traverse(root,depth):
            if not root:
                return
            if not root.left and not root.right:
                if depth > self.max_depth:
                    self.max_depth = depth
                    self.ans = [root.val]
                elif depth==self.max_depth:
                    self.ans.append(root.val)
            traverse(root.left,depth+1)
            traverse(root.right,depth+1)
        traverse(root,1)
        return self.ans[0]