from Node import Node
import random
from nose.tools import assert_equal


def cycle_check(head):
    faster = head
    slower = head

    while faster != None and faster.nextnode != None:
        slower = slower.nextnode
        faster = faster.nextnode.nextnode

        if faster == slower:
            return True
    return False


def create_cycled_noncycled_linked_list(list_length, cycle_at):
    head = Node(1)
    current_node = head

    node_length_checker = 0
    cycled_at_node = None
    for i in range(list_length):
        current_node.nextnode = Node(i)
        current_node = current_node.nextnode
        if node_length_checker == cycle_at:
            cycled_at_node = current_node

        node_length_checker += 1
    current_node.nextnode = cycled_at_node

    return head.nextnode


def print_node_values(head):
    while head != None:
        print(head.value)
        head = head.nextnode


def test():
    assert_equal(cycle_check(create_cycled_noncycled_linked_list(0, 0)), False)
    assert_equal(cycle_check(create_cycled_noncycled_linked_list(1, 0)), True)
    assert_equal(cycle_check(create_cycled_noncycled_linked_list(0, 1)), False)
    assert_equal(cycle_check(create_cycled_noncycled_linked_list(1, 1)), False)
    assert_equal(cycle_check(create_cycled_noncycled_linked_list(10, 9)), True)

    print("All passed")


test()
# print_node_values(create_cycled_noncycled_linked_list(5,0))