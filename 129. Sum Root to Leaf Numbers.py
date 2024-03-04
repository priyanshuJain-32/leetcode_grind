class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.paths = []
        self.ans = 0
        def traverse(root, path):
            if not root:
                return ""
            path += str(root.val)
            if not root.left and not root.right:
                self.ans += int(path)
                self.paths.append(path)
            traverse(root.left, path)
            traverse(root.right, path)
        traverse(root,"")
        return self.ans