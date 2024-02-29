class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        self.nums = set()
        def inorder(root):
            if not root:
                return set()
            inorder(root.left)
            self.nums.add(root.val)
            inorder(root.right)
        inorder(root)
        self.nums = list(self.nums)
        self.nums.sort()
        try:
            return self.nums[1]
        except:
            return -1