# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Google.
#
# Given the head of a singly linked list, reverse it in-place.


# Class that represents each node of the LL.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data  # returns the data when invoked


# Class that represents the LL. Start of Linked list is head and that's all we need.
class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        node = self.head  # First element
        nodes = []  # All elements

        # checks if the head is not empty, meaning linked list has no elements.
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("Empty")
        return " -> ".join(nodes)

    def rev(self):
        print()


if __name__ == '__main__':
    llist = LinkedList()
    first_node = Node("a")
    llist.head = first_node
    second_node = Node("b")
    third_node = Node("c")
    first_node.next = second_node
    second_node.next = third_node
    print(llist)
