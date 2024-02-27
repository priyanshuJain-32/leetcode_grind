class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def copyLeft(root):
            node = root.left
            root.val = node.val
            try: root.left = node.left
            except: root.left = None
            try: root.right = node.right
            except: root.right = None
            return root
        def copyRight(root):
            node = root.right
            root.val = node.val
            try: root.left = node.left
            except: root.left = None
            try: root.right = node.right
            except: root.right = None
            return root
        def minimum(root):
            if not root.left:
                return root
            return minimum(root.left)

        def delete(root,v):
            if not root:
                return
            elif root.val>v:
                root.left = delete(root.left, v)
                return root
            elif root.val<v:
                root.right = delete(root.right, v)
                return root
            elif root.val==v:
                if not(root.left or root.right):
                    root = None
                    return root
                elif not root.right:
                    root = copyLeft(root)
                elif not root.left:
                    root = copyRight(root)
                else:
                    minright = minimum(root.right)
                    root.val = minright.val
                    root.right = delete(root.right, minright.val)
                return root
        root = delete(root, key)
        return root