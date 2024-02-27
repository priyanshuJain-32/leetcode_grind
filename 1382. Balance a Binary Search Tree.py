class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        L = []
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            L.append(root.val)
            inorder(root.right)
        inorder(root)
        def constructTree(nums):
            n = len(nums)
            if n==0:
                return
            mid = n//2
            root = TreeNode(nums[mid])
            root.left = constructTree(nums[:mid])
            root.right = constructTree(nums[mid+1:])
            return root
        return constructTree(L)