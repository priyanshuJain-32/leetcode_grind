class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        self.path = []
        def traverse(root):
            if not root:
                return []
            self.path.append(root)
            traverse(root.left)
            traverse(root.right)
        traverse(root)
        if len(self.path)<=1:
            return
        prev = self.path[0]
        for node in self.path[1:]:
            prev.left = None
            prev.right = node
            prev = prev.right