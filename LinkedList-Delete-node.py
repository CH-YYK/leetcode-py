"""
you are given the head node from a linked list and the task is to build a function
that will delete a specific node
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
    def deletenode(self, head, val):
        if head.val == val:
            return head.next

        while head.next:
            if head.next.val == val:
                head.next = head.next.next
                return head
            else:
                head = head.next

        return head

class Solution:
    def removeNode(self, head, value):
        if head.val == value:
            return head.next
        tmp = head
        while tmp.next:
            if tmp.next.val == value:
                tmp.next = tmp.next.next
            else:
                tmp = tmp.next
        return head

if __name__ == '__main__':
    A = ListNode(2)
    A.appendToTail(2)
    A.appendToTail(1)
    ans = Solution().removeNode(A, 1)