# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans =  []

        def rec(node,path):
            if not node:
                return 
            
            if node:
                path = path + str(node.val)
                if not node.left and not node.right:
                    ans.append(path)
                    return
            
            

            rec(node.left,path)
            rec(node.right,path)
        
        rec(root,"")

        total = 0
        print(ans)
        for num in ans:
            num = int(num)
            total += num
        
        return total