class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def deleteLeaf(root):
            if not root:
                return
            root.left = deleteLeaf(root.left)
            root.right = deleteLeaf(root.right)
            if root.val == target and isleaf(root):
                return None
            return root
        def isleaf(root):
            return not root.left and not root.right
        return deleteLeaf(root)