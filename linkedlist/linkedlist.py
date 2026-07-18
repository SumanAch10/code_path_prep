class Node:
    def __init__(self,val,next):
        self.val = val
        self.next = None
    
class Linkedlist:
    def __init__(self):
        self.head = None
    
    #insert node at the end of the list
    def add_node(self,data):
        #insert at head
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
    
        curr = self.head
        
        while(curr.next):
            curr = curr.next
        
        curr.next = new_node
        
            
