class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        temp = head
        nums = []
        while temp:
            nums.append(temp.val)
            temp = temp.next
        def constructTree(nums):
            n = len(nums)
            if n==0:
                return
            mid = n//2
            root = TreeNode(nums[mid])
            root.left = constructTree(nums[:mid])
            root.right = constructTree(nums[mid+1:])
            return root
        return constructTree(nums)