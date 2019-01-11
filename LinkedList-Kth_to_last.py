"""
Implement an algorithm to find the kth to last element of a singly linked list

solution 1: linked size is known
solution 2: recursive
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
    def KthNodeToLast(self, head, k):
        diff = 0
        head2 = head
        while head.next:
            diff += 1
            head = head.next
            if diff >= k:
                head2 = head2.next
        return head2

    def KthToLast(self, head, k):
        if not head:
            return 0
        index = self.KthToLast(head.next, k) + 1
        if index == k:
            print(head.val)
        return index

if __name__ == '__main__':
    A = ListNode(1)
    A.appendToTail(2)
    A.appendToTail(1)
    print(Solution().KthNodeToLast(A, 3).val)