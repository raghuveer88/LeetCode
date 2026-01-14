# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = [root]
        node = root
        while node.left:
            self.stack.append(node.left)
            node = node.left


    def next(self) -> int:
        res = self.stack.pop()
        if res and res.right:
            self.stack.append(res.right)
            node = res.right
            while node.left:
                self.stack.append(node.left)
                node = node.left
        return res.val

    def hasNext(self) -> bool:
        if self.stack:
            return True
        else:
            return False
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()