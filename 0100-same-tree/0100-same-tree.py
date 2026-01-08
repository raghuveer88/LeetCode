# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if not p and not q:
            return True
        if not p or not q:
            return False

        q1 = deque([(p,"l")])
        q2 = deque([(q,"l")])

        while q1 and q2:

            for i in range(len(q2)):
                item1, side1 = q1.popleft()
                item2, side2 = q2.popleft()

                if not item1 and not item2:
                    continue
                if not item1 or not item2:
                    return False

                if item1.val != item2.val or side1 != side2:
                    return False

                
                q1.append((item1.left,"l"))
                
                q2.append((item2.left,"l"))
                
                q1.append((item1.right,"r"))
                
                q2.append((item2.right,"r"))
            
        if len(q1) != 0 or len(q2) != 0:
            return False
        
        return True








