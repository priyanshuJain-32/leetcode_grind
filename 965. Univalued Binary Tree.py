class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        self.count = 0
        self.total = 0
        def inorder(root):
            if not root:
                return 0
            self.total += root.val
            self.count += 1
            inorder(root.left)
            inorder(root.right)
        inorder(root)
        return self.total == root.val*self.count 