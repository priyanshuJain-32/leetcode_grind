class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            root = TreeNode(val)
        if val>root.val:
            root.right = self.insertIntoBST(root.right, val)
        if val<root.val:
            root.left = self.insertIntoBST(root.left, val)
        return root