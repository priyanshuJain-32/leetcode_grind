class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.ans = defaultdict(list)
        def traverse(root, depth):
            if not root:
                return
            self.ans[depth].append(root.val)
            traverse(root.left, depth+1)
            traverse(root.right, depth+1)
        traverse(root,0)
        return self.ans.values()