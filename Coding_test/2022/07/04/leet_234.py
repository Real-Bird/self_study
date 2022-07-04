class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, val):
        self.head = Node(val)

    def insert(self, val):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(val)


from collections import deque


def isPalindrome(head):
    q = deque([])
    if not head:
        return True

    Link = LinkedList(head[0])
    for i in range(1, len(head)):
        Link.insert(head[i])

    node = Link.head

    while node is not None:
        q.append(node.data)
        node = node.next

    while len(q) > 1:
        if q.popleft() != q.pop():
            return False

    return True


print(isPalindrome([1, 2, 2, 1]))
