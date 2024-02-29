class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        def findParentDepth(root, v, prev, depth):
            if not root:
                return
            if root.val==v:
                return (prev, depth)
            prev = str(root.val)
            depth += 1
            return findParentDepth(root.right, v, prev, depth) or findParentDepth(root.left, v, prev, depth)

        p1, d1 = findParentDepth(root, x, prev="_", depth=0)
        p2, d2 = findParentDepth(root, y, prev="_", depth=0)

        return p1!=p2 and d1==d2