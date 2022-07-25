class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Sll:
    def __init__(self):
        self.head = None
    
    def insert_at_last(self, data=None):
        if not data: return False
        new_node = Node(data)
        curr_head = self.head
        if not curr_head: 
            self.head = new_node
            return

        while(curr_head.next is not None):
            curr_head = curr_head.next
        curr_head.next = new_node
    
    def reverse(self):
        prev = None
        curr = self.head

        while(curr):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        self.head = prev
    
    def disp(self):
        curr_head = self.head
        while(curr_head):
            print(curr_head.data)
            curr_head = curr_head.next
    
    def ll(self):
        lst = []
        curr = self.head
        while(curr):
            lst.append(curr)
            curr = curr.next
        return lst


obj1 = Sll()
# obj2 = Sll()

obj1.insert_at_last(1)
obj1.insert_at_last(2)
obj1.insert_at_last(3)

print('Before')
obj1.disp()
print('--'*10)
obj1.reverse()

print('After')
obj1.disp()

# obj2.insert_at_last(4)
# obj2.insert_at_last(5)
# obj2.insert_at_last(6)

# lst1 = obj1.ll()
# lst2 = obj2.ll()
# res = []

# for v1, v2 in zip(lst1, lst2):
#     res.append(v1.data)
#     res.append(v2.data)
    
# print(res)