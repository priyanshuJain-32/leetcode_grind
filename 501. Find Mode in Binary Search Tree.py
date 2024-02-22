class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        D = defaultdict(int)
        def inorder(root):
            if not root:
                return
            nonlocal D
            inorder(root.left)
            D[root.val] += 1
            inorder(root.right)
        inorder(root)
        mode_freq = max(D.values())
        modes = []
        for k,v in D.items():
            if v==mode_freq:
                modes.append(k)
        return modes