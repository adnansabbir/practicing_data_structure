class BinaryTree(object):
    def __init__(self, root_object):
        self.key = root_object
        self.left_child = None
        self.right_child = None

    def insert_left(self, new_node):
        if not self.left_child:
            self.left_child = BinaryTree(new_node)
        else:
            temp_node = BinaryTree(new_node)
            temp_node.left_child = self.left_child
            self.left_child = temp_node
        return self.left_child

    def insert_right(self, new_node):
        if not self.right_child:
            self.right_child = BinaryTree(new_node)
        else:
            temp_node = BinaryTree(new_node)
            temp_node.right_child = self.right_child
            self.right_child = temp_node
        return self.right_child

    def get_right_child(self):
        return self.right_child

    def get_left_child(self):
        return self.left_child

    def set_root_value(self, root_object):
        self.key = root_object

    def get_root_value(self):
        return self.key

    def __str__(self):
        return '{}'.format(self.key)

    def print_tree(self, height=4):
        nodes = []
        print(self.key)
        nodes.append(self.left_child)
        nodes.append(self.right_child)

        for i in range(height):

            list_length = len(nodes)
            for node in nodes:
                if type(node) == type(self):
                    nodes.append(node.left_child)
                    nodes.append(node.right_child)
            node_line = ""
            for node in range(list_length):
                node_line += str(nodes.pop(0) or " ")
            print(node_line)
