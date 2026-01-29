class Node():
    def __init__(self):
        self.endswith = False
        self.children = {}

class Trie:

    def __init__(self):
        self.root = Node()
        
    def insert(self, word: str) -> None:
        curr = self.root
        for i in range(len(word)):
            if word[i] not in curr.children:
                curr.children[word[i]] = Node()
            curr = curr.children[word[i]]
        curr.endswith = True

    def search(self, word: str) -> bool:
        curr = self.root
        for i in range(len(word)):
            if word[i] not in curr.children:
                return False
            
            curr = curr.children[word[i]]
        if curr.endswith:
            return True
        return False
            

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for i in range(len(prefix)):
            if prefix[i] not in curr.children:
                return False
            curr = curr.children[prefix[i]]
        
        return True
                  


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)