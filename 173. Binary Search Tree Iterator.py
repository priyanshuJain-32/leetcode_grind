class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.tree = [TreeNode(-1)]
        self.idx = 0
        def inorder(root):
            if not root:
                return []
            inorder(root.left)
            self.tree.append(root)
            inorder(root.right)
        inorder(root)

    def next(self) -> int:
        self.idx += 1
        return self.tree[self.idx].val
        
    def hasNext(self) -> bool:
        return self.idx<len(self.tree)-1