class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.dict = defaultdict(list)
        def traverse(root,depth):
            if not root:
                return
            self.dict[depth].append(root.val)
            traverse(root.left, depth+1)
            traverse(root.right, depth+1)
        traverse(root,0)
        return reversed(self.dict.values())