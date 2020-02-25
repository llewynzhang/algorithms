class Node:
    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.d = {}
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        # check if key is in d
        if key in self.d:
            # if is inside, get value, move to head
            node = self.d[key] 
            self.removeNode(node)
            self.addHead(node)
            return node.val
        # else return -1
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        # check if key is in d
        if key in self.d:
            # if so update value
            node = self.d[key]
            node.val = value
            # move it to the head
            self.removeNode(node)
            self.addHead(node)
        # else create new entry in d
        else:
            node = Node(key, value)
            # add new node to the head & d
            self.addHead(node)
            self.d[key] = node
            # check capacity
            if len(self.d) > self.capacity:
                self.popTail()
    
    # remove the node at given 
    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        
    # add the node at the head of the list
    def addHead(self, node):
        node.prev = self.head
        node.next = self.head.next
        node.next.prev = node
        node.prev.next = node
    
    # remove the node at the tail of the list
    def popTail(self):
        node = self.tail.prev
        del self.d[node.key]
        self.tail.prev = self.tail.prev.prev
        self.tail.prev.next = self.tail


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)