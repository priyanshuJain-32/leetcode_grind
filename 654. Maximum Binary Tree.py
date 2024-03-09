class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        # base case
        if not nums:
            return 
        maxi = -1
        idx = 0
        for i in range(len(nums)):
            if nums[i]>maxi:
                maxi = nums[i]
                idx = i
        root = TreeNode(maxi)
        root.left = self.constructMaximumBinaryTree(nums[:idx])
        root.right = self.constructMaximumBinaryTree(nums[idx+1:])
        return root