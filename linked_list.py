class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.current = None
        self.head = None

    # For our task purpose it is required to work with LinkedList, so convert user-provided list to LinkedList
    def populate(self, lst):
        [self.addEnd(i) for i in lst]

    def addBegin(self, data):
        new_node = Node(data)
        new_node.next = self.head  # new node points to old head
        self.head = new_node  # new head points to new node

    def addEnd(self, data):
        new_node = Node(data)

        if self.head is None:  # if list empty
            self.head = new_node
            return

        last = self.head  # last node is head if there is only in val  in the list
        while last.next:  # otherwise iterate from head to get last node in the list
            last = last.next
        last.next = new_node

    def traverse(self):
        temp_node = self.head
        print('[', end='')
        while temp_node:
            print(str(temp_node.val), end="")
            temp_node = temp_node.next
            if temp_node:
                print(",", end='')
        print(']')

    # return list for assertion purposes, not LinkedList
    def get_list(self):
        temp_node = self.head
        res = []
        while temp_node:
            res.append(temp_node.val)
            temp_node = temp_node.next
        return res

    # Overriding comparison "==" operator
    def __eq__(self, other):
        first = self.head
        second = other.head
        try:
            while first:
                if first.val != second.val:
                    return False
                first = first.next
                second = second.next
        except ValueError:
            return False
        return True

    def __str__(self):
        return self.traverse()
