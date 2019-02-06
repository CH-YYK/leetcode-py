# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # O(n) in time, O(n) in space
        stack = []
        tmp = head
        while tmp:
            stack.append(tmp.val)
            tmp = tmp.next

        while stack:
            value = stack.pop()
            if not value == head.val:
                return False
            head = head.next
        return True

    def isPalindrome_reverse(self, head):
        # O(n) in time, O(1) in space
        prev = None
        fast = head
        middle = head
        while fast and fast.next:
            # update `fast` to avoid being violated
            fast = fast.next.next

            # reverse links
            tmp = middle.next
            middle.next = prev
            prev = middle
            middle = tmp

        if fast is None:  # even number
            while prev and middle:
                if not prev.val == middle.val:
                    return False
                prev = prev.next
                middle = middle.next

        else:  # odd number
            middle = middle.next
            while prev and middle:
                if not prev.val == middle.val:
                    return False
                prev = prev.next
                middle = middle.next
        return True