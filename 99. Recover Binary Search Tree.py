class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        def find(root,v):
            if not root:
                return -1
            if root.val == v:
                return root
            left = find(root.left, v)
            right = find(root.right, v)
            return left if left!=-1 else right
        org_nums = []
        def inorder(root):
            if not root:
                return
            nonlocal org_nums
            inorder(root.left)
            org_nums.append(root.val)
            inorder(root.right)
        
        inorder(root)
        sorted_nums = sorted(org_nums)
        to_swap = []
        for i, j in zip(org_nums, sorted_nums):
            if i-j!=0:
                to_swap.append(i)
                to_swap.append(j)
                break
        a = find(root, to_swap[0])
        b = find(root, to_swap[1])
        a.val, b.val = b.val, a.val