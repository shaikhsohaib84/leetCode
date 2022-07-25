class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self, data=None):
        if not data: return False
        new_node = Node(data)
        curr = self.head

        if not self.head:
            self.head = new_node
            return
        
        while(curr.next):
            curr = curr.next
        
        curr.next = new_node
    
    def middleLinkedList(self):
        size = 0
        curr = self.head

        while curr:
            size += 1
            curr = curr.next

        curr = self.head
        
        for node in range(0, size//2):
            curr = curr.next

        self.head = curr

    def disp(self):
        curr = self.head
        while curr:
            print('data', curr.data)
            curr = curr.next

obj = SinglyLinkedList()
obj.insert(1)
obj.insert(2)
obj.insert(3)
obj.insert(4)
obj.insert(5)
# obj.insert(6)

print('Before')
obj.disp()
obj.middleLinkedList()
print('\n')
print('After')
obj.disp()