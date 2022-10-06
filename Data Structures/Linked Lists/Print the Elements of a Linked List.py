# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next

head=[2,16,13]
# data=[16,13]

def SinglyLinkedListNode(head): 
    while head!=None:
        print(head.data)
        head=head.next 

print(SinglyLinkedListNode())

        
# SinglyLinkedListNode(16)
# ih=2
# id=[16,13]

# def print_list(ih):
#     while(ih!=None):
#         print(ih.data)
#         ih=ih.next

