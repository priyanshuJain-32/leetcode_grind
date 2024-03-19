class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.total = 0
        def givegc(root):
            total = 0
            if root.left:
                if root.left.left:
                    total += root.left.left.val
                if root.left.right:
                    total += root.left.right.val
            if root.right:
                if root.right.left:
                    total += root.right.left.val
                if root.right.right:
                    total += root.right.right.val
            return total
        def traverse(root):
            if not root:
                return [0]
            if root.val%2==0:
                self.total+=givegc(root)
            traverse(root.left)
            traverse(root.right)
        
        traverse(root)
        return self.total