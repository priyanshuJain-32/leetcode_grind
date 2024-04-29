class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.vals = set()
        def convert(root,v):
            if not root:
                return 
            root.val = v
            self.vals.add(v)
            root.left = convert(root.left,2*v+1)
            root.right = convert(root.right,2*v+2)
            return root
        self.tree = convert(root,0)

    def find(self, target: int) -> bool:
        return target in self.vals
        # def search(root,target):
        #     if not root:
        #         return False
        #     if root.val == target:
        #         return True
        #     return search(root.left,target) or search(root.right,target)
        # return search(self.tree,target)