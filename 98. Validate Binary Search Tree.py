class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def inorder(root):
            if not root:
                return []
            return inorder(root.left) + [root.val] + inorder(root.right)
        vals = inorder(root)
        for i in range(len(vals)-1):
            if not vals[i]<vals[i+1]:
                return False
        return True