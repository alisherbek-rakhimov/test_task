from linked_list import LinkedList


# in1 = input().split(',')
# in2 = input().split(',')


def add_lists(list1, list2):
    l1 = LinkedList()
    l2 = LinkedList()

    l1.populate(list1)
    l2.populate(list2)

    res = LinkedList()
    l1_head = l1.head
    l2_head = l2.head
    carry = 0

    while l1_head is not None or l2_head is not None:
        x = l1_head.val if l1_head else 0
        y = l2_head.val if l2_head else 0
        # print("x:", x, "y:", y, "carry: ", carry)
        sum = carry + x + y
        carry = sum // 10

        res.addEnd(sum % 10)
        l1_head = l1_head.next if l1_head else None
        l2_head = l2_head.next if l2_head else None

    if carry:
        res.addEnd(carry)

    return res


def test(l1, l2, l3):
    print('----------------TESTING----------------')
    ll = LinkedList()
    ll.populate(l3)
    assert add_lists(l1, l2) == ll


test([2, 4, 3], [5, 6, 4], [7, 0, 8])
test([0], [0], [0])
test([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9], [8, 9, 9, 9, 0, 0, 0, 1])
test([1, 2, 3], [4, 5, 6], [5, 7, 9])
test([7, 5, 9, 4, 6], [8, 4], [5, 0, 0, 5, 6])
test([5, 6, 3], [8, 4, 2], [3, 1, 6])
