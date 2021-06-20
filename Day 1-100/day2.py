'''

Given a linked list of numbers and a pivot k, partition the linked list so that all nodes less than k come before nodes greater than or equal to k.

For example, given the linked list 5 -> 1 -> 8 -> 0 -> 3 and k = 3, the solution could be 1 -> 0 -> 5 -> 8 -> 3.
'''

# TODO : k is an item from the list, k se chote wale number inserted first, rest of items are inserted as it is.

from day1 import LinkedList, Node

class LL(LinkedList):
    def __iter__(self):
        node = self.head   # Set a head, where to start from
        while node is not None:
            yield node
            node = node.next

    def add_first(self, node):
        node.next = self.head  # New Node's next = current head
        self.head = node       # New Head is new node added in begginning of LL.

    def remove_node(self, target_node_data):
        '''
        :param target_node_data:
        :return:

        Traverse to find the node you want, then link the target node's previous and target nodes's next together.
        Basically relinking.
        '''
        # Case 1:
        if self.head is None:
            raise Exception('List is Empty')

        # Case 2:
        if self.head == target_node_data:
            self.head = self.head.next
            return
        previous_node = self.head

        # Case 3:
        for node in self:
            if node.data == target_node_data:
                previous_node.next = node.next
                return
            previous_node = node
        raise Exception("Node with data '%s' not found" % target_node_data)



if __name__ == '__main__':
    llist = LL(['5', '1', '8', '0', '3'])
    k = 3
    print('The List is {}, and the pivot is {}'.format(llist, k))
    # first_node = Node("a")
    # llist.head = first_node
    # second_node = Node("b")
    # third_node = Node("c")
    # first_node.next = second_node
    # second_node.next = third_node
    removed_nodes = []
    for node in llist:
        if int(node.data) < k:
            removed_nodes.append(node.data)
            llist.remove_node(node.data)
    for i in reversed(removed_nodes):
        n = Node(i)
        llist.add_first(n)
    print(llist)