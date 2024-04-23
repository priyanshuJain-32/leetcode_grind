class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.count = 0
        def sumCount(root):
            if not root:
                return 0,0
            left,nl = sumCount(root.left)
            right,nr = sumCount(root.right)
            if (left+right+root.val)//(nl+nr+1)==root.val:
                self.count+=1
            return left+right+root.val,nl+nr+1
        sumCount(root)
        return self.count