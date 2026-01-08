class Node:
    def __init__(self,key,val=0,next=None,prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = {}
        self.tail = Node(-1,-1)
        self.head = Node(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head


    def get(self, key: int) -> int:
        if key not in self.hashmap:
            return -1
        node = self.hashmap[key]
        val = node.val
        self.delnode(node)
        self.insert(node)

        return val


    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            node = self.hashmap[key]
            node.val = value
            self.delnode(node)
            self.insert(node)
            return
        

        elif len(self.hashmap) >= self.capacity:
            temp =self.tail.prev
            del self.hashmap[temp.key]
            self.delnode(temp)
            
        node = Node(key,value)
        self.hashmap[key] = node
        self.insert(node)
            


    def delnode(self,node):
        temp = node.prev
        nxt = node.next
        temp.next = nxt
        nxt.prev = temp
    
    def insert(self,node):
        after = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = after
        after.prev = node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)