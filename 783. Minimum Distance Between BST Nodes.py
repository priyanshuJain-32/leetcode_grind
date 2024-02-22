class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        def inorder(root):
            if not root:
                return []
            return inorder(root.left) + [root.val] + inorder(root.right)
        L = inorder(root)
        mini = 1000000
        for i in range(len(L)-1):
            mini = min(mini, L[i+1]-L[i])
        return mini