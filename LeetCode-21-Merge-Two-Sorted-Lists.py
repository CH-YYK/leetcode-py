# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: 'ListNode', l2: 'ListNode') -> 'ListNode':
        """
        O(N) in time, O(1) in space
        """
        newList = ListNode(0)
        curr = newList
        while l1 or l2:
            if l1 and l2:
                if l1.val < l2.val:
                    curr.next = l1
                    curr = curr.next
                    l1 = curr.next
                else:
                    curr.next = l2
                    curr = curr.next
                    l2 = curr.next
            else:
                curr.next = l1 if l1 else l2
                if l1:
                    curr.next = l1
                    curr = curr.next
                    l1 = curr.next
                else:
                    curr.next = l2
                    curr = curr.next
                    l2 = curr.next
        return newList.next

    def mergeTwoLists2(self, l1: 'ListNode', l2: 'ListNode') -> 'ListNode':
        """
        using stack
        """
        if l1.val < l2.val:
            stack = [l1]
            l1 = l1.next
        else:
            stack = [l2]
            l2 = l2.next

        newList = ListNode(0)
        curr = newList
        while stack:
            node = stack.pop()
            curr.next = node
            curr = curr.next

            if l1 and l2:
                if l1.val < l2.val:
                    stack.append(l1)
                    l1 = l1.next
                else:
                    stack.append(l2)
                    l2 = l2.next
            else:
                curr.next = l1 if l1 else l2
        return newList.next
