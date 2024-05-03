class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.view = defaultdict(int)
        def travel(root,depth):
            if not root:
                return
            self.view[depth] = root.val
            travel(root.left,depth+1)
            travel(root.right,depth+1)
        travel(root,1)
        return self.view.values()