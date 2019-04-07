from Trees.BinaryTree import BinaryTree
from Trees.binary_tree_traversal import preorder, postorder, inorder

bin_tree = BinaryTree(1)
left_child1 = bin_tree.insert_left(2)
right_child2 = bin_tree.insert_right(3)

left_child1.insert_left(4)
left_child1.insert_right(5)

right_child2.insert_left(6)
right_child2.insert_right(7)
bin_tree.print_tree()

# preorder(bin_tree)
# postorder(bin_tree)
# inorder(bin_tree)
#
# list = [1,2,3,4]
# print(list.pop())
# list.insert(0,5)
# print(list)