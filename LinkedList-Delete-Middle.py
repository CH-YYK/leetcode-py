"""
Implement an algorithm to delete a node in the middle
solution: three object: previous, current, middle
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
    def deleteMiddle(self, head):
        current = head
        middle = head
        pre = ListNode(None)
        pre.next = head
        index = 0
        while current.next:
            index += 1
            if index > 0 and index % 2 == 0:
                middle = middle.next
                pre = pre.next
            current = current.next
        pre.next = pre.next.next
        return head

if __name__ == '__main__':
    A = ListNode(1)
    A.appendToTail(2)
    A.appendToTail(1)
    ans = Solution().deleteMiddle(A)