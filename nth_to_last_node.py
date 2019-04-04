from Node import Node
def nth_to_last_node(n, head):
    last_node = head
    for i in range(n-1):
        if not last_node.nextnode:
            raise LookupError("Error: n is larger then the linked list")
        last_node = last_node.nextnode

    n_minus_last_node = head
    while last_node.nextnode:
        last_node = last_node.nextnode
        n_minus_last_node = n_minus_last_node.nextnode
    return n_minus_last_node

