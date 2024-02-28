class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        self.count = 0
        def traverse(root):
            if not root:
                return
            self.count += 1
            traverse(root.left)
            traverse(root.right)
        traverse(root)
        return self.count