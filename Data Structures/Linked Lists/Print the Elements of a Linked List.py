
'''origin example'''
# def SinglyLinkedListNode(head):
#     while head!=None:
#         print(head.data)
#         head=head.next

'''class example'''
# class Linked_list:
#     def __init__(self) -> None:
#         self.head = None

#     def __repr__(self) -> str:
#         node=self.head
#         nodes=[]
#         while node is not None:
#             nodes.append(node.data)
#             node=node.next
#         nodes.append("None")
#         return " -> ".join(nodes)


# class Node:
#     def __init__(self, data) -> None:
#         self.data = data
#         self.next = None

#     def __repr__(self) -> str:
#         return self.data


# llist = Linked_list()
# first_node = Node("a")
# llist.head = first_node
# second_node = Node("b")
# third_node = Node("c")
# first_node.next = second_node
# second_node.next = third_node
# print(llist)

class Linked_list:
    def __init__(self,nodes=None) -> None:
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next

    def __repr__(self) -> str:
        node=self.head
        nodes=[]
        while node is not None:
            nodes.append(node.data)
            node=node.next
        nodes.append("None")
        return " -> ".join(nodes)

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

    def __repr__(self) -> str:
        return self.data


llist=Linked_list(["a","b","c","d","e"])
print(llist)

for node in llist:
    print(node)

'''traverse'''



