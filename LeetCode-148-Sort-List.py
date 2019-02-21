# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def sortList(self, head: 'ListNode') -> 'ListNode':
        # merge sort
        return self.mergeSort(head)

    def merge(self, head1, head2):
        # merge two sorted list
        newNode = ListNode(0)
        curr = newNode
        while head1 and head2:
            if head1.val < head2.val:
                curr.next = head1
                head1 = head1.next
            else:
                curr.next = head2
                head2 = head2.next
            curr = curr.next

        curr.next = head1 if head1 else head2
        return newNode.next

    def mergeSort(self, head):
        if not head or not head.next:
            return head
        # find mid point
        cur = head
        mid = head
        pre = head
        while cur and cur.next:
            pre = mid
            mid = mid.next
            cur = cur.next.next
        head2 = pre.next
        pre.next = None

        h1 = self.mergeSort(head)
        h2 = self.mergeSort(head2)
        return self.merge(h1, h2)