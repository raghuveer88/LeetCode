class TrieNode:
    def __init__(self):
        self.children = {}
        self.top3 = []

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self,word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()

            node = node.children[c]

            if len(node.top3) < 3:
                node.top3.append(word)

    def query(self,prefix):
        node = self.root
        
        for c in prefix:
            if c not in node.children:
                return []
            node = node.children[c]
        
        return node.top3
        
        


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:

        products.sort()
        trie = Trie()

        for p in products:
            trie.insert(p)

        prefix = ""
        res = []

        for c in searchWord:
            prefix += c
            res.append(trie.query(prefix))

        return res

        
