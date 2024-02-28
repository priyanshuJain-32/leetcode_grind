class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []
        def traverse(root, path):
            if not root:
                return ""
            if not root.left and not root.right:
                path += str(root.val)
                ans.append(path)
            else:
                path += str(root.val) + "->"
            traverse(root.left, path)
            traverse(root.right, path)
        traverse(root, "")
        return ans