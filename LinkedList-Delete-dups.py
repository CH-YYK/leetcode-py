"""
you are given a head Node from a linked list, now remove the duplicates in this Linked list
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def appendToTail(self, x):
        tmp = ListNode(x)
        n = self
        while n.next:
            n = n.next
        n.next = tmp


class Solution:
    def removeDups(self, head):
        values = {head.val: True}
        while head and head.next:
            if head.next.val in values:
                head.next = head.next.next
            else:
                values[head.next.val] = True
            head = head.next
        print(values)

    # O(n) in time and O(n) in space
    def removeDups_pre(self, head):
        values = {}
        previous = ListNode(None)
        while head:
            if head.val in values:
                previous.next = head.next
            else:
                values[head.val] = True
            head = head.next

if __name__ == '__main__':
    A = ListNode(1)
    A.appendToTail(2)
    A.appendToTail(1)
    ans = Solution().removeDups(A)



