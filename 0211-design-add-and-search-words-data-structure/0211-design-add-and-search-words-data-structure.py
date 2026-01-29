class Node():
    def __init__(self):
        self.children = {}
        self.endword = False

class WordDictionary:

    def __init__(self):
        self.root = Node()
        

    def addWord(self, word: str) -> None:
        curr = self.root
        for i in range(len(word)):
            if word[i] not in curr.children:
                curr.children[word[i]] = Node()
            curr = curr.children[word[i]]
        curr.endword = True

    
    def search(self, word: str) -> bool:
        
        def rec(idx: int, curr: Node) -> bool:
            if idx == len(word):
                return curr.endword

            ch = word[idx]
            if ch == '.':
                for nxt in curr.children.values():
                    if rec(idx + 1, nxt):
                        return True
                return False
            else:
                if ch not in curr.children:
                    return False
                return rec(idx + 1, curr.children[ch])

        return rec(0, self.root)

        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)