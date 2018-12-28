"""
Given a Linked list, print the node that is last but 2 in list.
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def Find3rdfromEnd(self, head):
        target = head
        current = head
        length = 0

        while current.next:
            length += 1
            current = current.next
            if length >= 3:
                target = target.next
        return target.val


if __name__ == '__main__':
    p1 = ListNode(1)
    p2 = ListNode(2)
    p3 = ListNode(3)
    p4 = ListNode(4)
    p5 = ListNode(5)

    p1.next = p2
    p2.next = p3
    p3.next = p4
    p4.next = p5

    print(Solution().Find3rdfromEnd(p1))