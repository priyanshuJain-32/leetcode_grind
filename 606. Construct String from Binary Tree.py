class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def convert(root):
            if not root:
                return '()'
            if not root.left and not root.right:
                return '('+str(root.val)+')'
            left = convert(root.left)
            right = convert(root.right)
            if right=='()':
                string = '(' + str(root.val) + left +')'
            else:
                string = '(' + str(root.val) + left + right +')'
            return string
        return convert(root)[1:-1]