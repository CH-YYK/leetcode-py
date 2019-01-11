"""
You are given a head node from a linked list, implement an algorithms to partition
the list by an integer
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
    def partition(self, node, x):
        head = node
        tail = node

        while node:
            next = node.next
            if node.val < x:
                node.next = head
                head = node
            else:
                tail.next = node
                tail = node
            node = next
        tail.next = None
        return head


if __name__ == '__main__':
    A = ListNode(1)
    A.appendToTail(2)
    A.appendToTail(3)
    A.appendToTail(4)
    A.appendToTail(2)

    ans = Solution().partition(A, 3)