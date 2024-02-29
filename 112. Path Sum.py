class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        self.result = False
        def traverse(root, path):
            if not root:
                return
            path += root.val
            if not root.left and not root.right:
                if path==targetSum:
                    self.result = True
            elif root:
                traverse(root.left, path)
                traverse(root.right, path)
        traverse(root, 0)
        return self.result