class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        self.ans = []
        self.to_delete = set(to_delete)
        def delete(root):
            if not root:
                return
            root.left = delete(root.left)
            root.right = delete(root.right)
            if root.val in self.to_delete:
                if root.left:
                    self.ans.append(root.left)
                if root.right:
                    self.ans.append(root.right)
                return
            return root
        root = delete(root)
        if root:
            self.ans.append(root)
        return self.ans