class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self, head):
        self.head = head

    def display_linkedlist(self):
        current = self.head
        while current:
            print(current.data, end=", ")
            current = current.next

    def insert_head_node(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_tail_node(self,data):
        new_node = Node(data)
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def insert_at_position(self,data,position):
        new_node = Node(data)
        current = self.head
        for i in range (1,position-1):
            current = current.next
        new_node.next = current.next
        current.next = new_node

    # get a specific node's data
    def get_nthnode_data(self, position):
        current = self.head
        counter = 1
        while counter < position:
            counter+= 1
            current = current.next
        return current.data

    def delete_head(self):
        self.head = self.head.next

    def delete_tail(self):
        current = self.head
        while current.next.next:
            current = current.next
        current.next = None

    def delete_intermediate_node(self,position):
        current = self.head
        counter = 1
        while counter < position-1:
            counter += 1
            current = current.next
        current.next= current.next.next

llist = LinkedList(Node("Node-1 Data"))
print()
llist.display_linkedlist()
llist.insert_head_node("Node-2 Data")
print()
llist.display_linkedlist()
llist.insert_tail_node("Node-3  Data")
print()
llist.display_linkedlist()
llist.insert_at_position("Node-4  Data",3)
print()
llist.display_linkedlist()
print()
print(f"Value of 3rd node: {llist.get_nthnode_data(3)}")

#llist.delete_head()
#print()
#llist.display_linkedlist()
#delete head

#delete tail
#llist.delete_tail()
print()
#llist.display_linkedlist()
llist.delete_intermediate_node(3)
llist.display_linkedlist()
#delete an intermediate node