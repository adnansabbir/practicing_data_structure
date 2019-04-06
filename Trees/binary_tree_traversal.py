from Trees.BinaryTree import BinaryTree


def preorder(tree: BinaryTree):
    if tree:
        print(tree.get_root_value())
        preorder(tree.left_child)
        preorder(tree.right_child)


def postorder(tree: BinaryTree):
    if tree:
        postorder(tree.left_child)
        postorder(tree.right_child)
        print(tree.get_root_value())


def inorder(tree: BinaryTree):
    if tree:
        inorder(tree.left_child)
        print(tree.get_root_value())
        inorder(tree.right_child)
