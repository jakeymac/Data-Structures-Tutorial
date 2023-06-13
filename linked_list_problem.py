class LinkedList:
    #Class to form a new node, or element of a linked list
    class Node:
        def __init__(self,data,next=None,previous=None):
            self.data = data
            self.next = next
            self.previous = previous
    
    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None

    #Method to insert a node at the beginning of a linked list
    def insert_head(self,data):
        #In case the linked list does not already have a head node
        if self.head is None:
            self.head = LinkedList.Node(data)
            self.tail = self.head

        #In case the linked list does already have a head node
        else:
            old_head = self.head
            self.head = Node(data,next=old_head)
            old_head.previous = self.head

        self.length += 1

    #Method to insert a node at the end of a linked list
    def insert_tail(self,data):
        #In case the linked list does not already have a tail node
        if self.tail is None:
            self.tail = LinkedList.Node(data,previous=self.head)
            self.head.next=self.tail
        #In case the linked list does already have a tail node.
        else:
            new_node = LinkedList.Node(data,previous=self.tail)
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1

    #Method to insert a node at whichever location desired according to the nodes it'll go between.
    def insert_node(self,data,previous,next):
        new_node = LinkedList.Node(data,previous,next)
        previous.next = new_node
        next.previous = new_node

        self.length += 1
    
    #Method to insert a node at a desired index in the linked list
    def insert_node_at_index(self,data,index):
        if index == 0:
            self.insert_head(self,data)

        elif index == self.length:
            self.insert_tail(self,data)
        
        else:
            current_node = self.head
            current_num = 1
            while current_num != index:
                current_node = current_node.next
                current_num += 1

            new_node = LinkedList.Node(data,previous=current_node,next=current_node.previous)
            current_node.next.previous = new_node
            current_node.next = new_node
            self.length += 1

    
    #Method to display a linked list's nodes. 
    def display_list(self):
        curr = self.head
        while curr is not None:
            print(curr.data)
            curr = curr.next

    def search_list():
        #Add your own code here to check if this a linked list 
        #contains a node with a certain value
        pass

test_1_list = LinkedList()
test_1_list.insert_head(5)
test_1_list.insert_tail(17)
test_1_numbers = [13,9,16,2,7]
for num in test_1_numbers:
    test_1_list.insert_tail(num)

#These tests should all pass as long as your function has been done correctly
assert test_1_list.search_list(9) == True 
assert test_1_list.search_list(12) == False
test_1_list.insert_node(12,test_1_list.tail.previous,test_1_list.tail)
assert test_1_list.search_list(12) == True

