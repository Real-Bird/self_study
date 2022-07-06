def reverseList(head):
    def reverse(node, prev):
        if not node:
            return prev
        next, node.next = node.next, prev
        return reverse(next, node)
    return reverse(head)