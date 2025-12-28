class TreeNode:
    def __init__(self):
        self.children = {}
        self.isend = False
class Trie:
    def __init__(self):
        self.root = TreeNode()
    def insert(self,word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TreeNode()
            curr = curr.children[char]
        curr.isend = True
    def check(self,arr):
        curr = self.root
        res = ""
        word = arr[0]
        for char in word:
            if len(curr.children) == 1 and not curr.isend:
                res += char
                curr = curr.children[char]
            
        return res
                

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        obj = Trie()
        for s in strs:
            obj.insert(s)
        
        return obj.check(strs)

        