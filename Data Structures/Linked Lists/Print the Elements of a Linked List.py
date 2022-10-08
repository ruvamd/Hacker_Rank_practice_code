

# def SinglyLinkedListNode(head):
#     while head!=None:
#         print(head.data)
#         head=head.next

class singly_linked_list:
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0
    def print_list(self):
        '''print the linked list'''
        temp=self.head
        while temp is not None:
            print(temp.data)
            temp=temp.next
    def insert(self,data):
        '''insert a node at the end'''
        new_node=singly_linked_list_node(data) 
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            self.tail=new_node
        self.length+=1
        return self
    def prepend(self,data):
        '''insert a node at the beginning'''
        new_node=singly_linked_list_node(data)
        new_node.next=self.head
        self.head=new_node
        self.length+=1
        return self
    def insert_at(self,data,index):
        '''insert a node at a given index'''
        if index>=self.length:
            return self.insert(data)
        if index==0:
            return self.prepend(data)
        new_node=singly_linked_list_node(data)
        leader=self.traverse_to_index(index-1)
        holding_pointer=leader.next
        leader.next=new_node
        new_node.next=holding_pointer
        self.length+=1
        return self
    def traverse_to_index(self,index):
        '''traverse to a given index'''
        counter=0
        current_node=self.head
        while counter!=index:
            current_node=current_node.next
            counter+=1
        return current_node
    def remove_at(self,index):
        '''remove a node at a given index'''
        if index>=self.length:
            print("Index out of range")
            return
        if index==0:
            self.head=self.head.next
            self.length-=1
            return self
        leader=self.traverse_to_index(index-1)
        leader.next=leader.next.next
        self.length-=1
        return self
    def reverse(self):
        '''reverse the linked list'''
        if not self.head.next:
            return self.head
        first=self.head
        self.tail=self.head
        second=first.next
        while second:
            temp=second.next
            second.next=first
            first=second
            second=temp
        self.head.next=None
        self.head=first
        return self





