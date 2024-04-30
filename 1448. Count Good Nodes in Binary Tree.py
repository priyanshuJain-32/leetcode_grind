class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
        def traverse(root,high):
            if not root:
                return
            if root.val>high:
                self.count+=1
                high = root.val
            elif root.val==high:
                self.count += 1
            traverse(root.left,high)
            traverse(root.right,high)
        traverse(root,root.val)
        return self.count