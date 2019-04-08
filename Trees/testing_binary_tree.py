from Trees.BinaryTree import BinaryTree
from Trees.binary_tree_traversal import preorder, postorder, inorder


def level_order_print(tree):
    nodes = [tree]
    nodes_length = 1
    while nodes_length:
        nodes_length = len(nodes)
        if nodes_length == 0:
            break
        parent_nodes = []
        for i in range(nodes_length):
            parent_nodes.append(nodes.pop(0))
        print(' '.join([parent.__str__() for parent in parent_nodes]))
        for parent in parent_nodes:
            nodes = nodes+get_childs(parent)

def get_childs(node):
    childs = []

    if not node:
        childs

    if node.left_child:
        childs.append(node.left_child)

    if node.right_child:
        childs.append(node.right_child)

    return childs



bin_tree = BinaryTree(1)
left_child1 = bin_tree.insert_left(2)
right_child2 = bin_tree.insert_right(3)

left_child1.insert_left(4)
left_child1.insert_right(5)

right_child2.insert_left(6)
right_child2.insert_right(7)

level_order_print(bin_tree)



# preorder(bin_tree)
# postorder(bin_tree)
# inorder(bin_tree)
#
# list = [1,2,3,4]
# print(list.pop())
# list.insert(0,5)
# print(list)