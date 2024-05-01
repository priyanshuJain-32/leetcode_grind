class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def traverse(root,counts):
            if not root:
                return
            counts[root.val] += 1
            if not root.left and not root.right:
                if self.checkPalindrome(counts):
                    self.ans += 1
            traverse(root.left,counts.copy())
            traverse(root.right,counts.copy())
        traverse(root,defaultdict(int))
        return self.ans
        
    def checkPalindrome(self,counts):
        odd_count = 0
        for v in counts.values():
            if v%2:
                odd_count += 1
        return odd_count <= 1