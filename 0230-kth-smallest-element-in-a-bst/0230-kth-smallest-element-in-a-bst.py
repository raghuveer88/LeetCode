# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # In the problem he gave that it is a binary tree. so if we do inorder traversing then
    # we get a sorted array. once we get try to return the kth smallest number 
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res_arr = []
        res_arr = self.dsf(root, res_arr)
        # res_arr.sort()
        return res_arr[k-1]

    def dsf(self, root: Optional[TreeNode], res_arr):
        if not root:
            return 
        self.dsf(root.left, res_arr)
        res_arr.append(root.val)
        self.dsf(root.right, res_arr)
        return res_arr
        

        