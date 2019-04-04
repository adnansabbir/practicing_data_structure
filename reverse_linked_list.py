from Node import Node

def reverse_linked_list(head):
    if head.nextnode and head.nextnode.nextnode:
        a = head
        b = a.nextnode
        c = b.nextnode

        while c != None:
            b.nextnode = a

            a = b
            b = c
            c = c.nextnode

        b.nextnode = a
        head.nextnode = None
        return b
    elif head.nextnode:
        a = head.nextnode
        a.nextnode = head
        head.nextnode = None
        return a
    else:
        return head
