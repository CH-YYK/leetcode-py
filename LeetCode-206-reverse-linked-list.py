class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # Iterative solution
    def reverseList(self, head: ListNode) -> ListNode:
        pre = None
        while head:
            tmp = head.next
            head.next = pre
            pre = head
            head = tmp
        return pre

class Solution2:
    # recursive solution
    def reverseList(self, head):
        return self.reverseRecur(head, None)

    def reverseRecur(self, curr, pre):
        if not curr:
            return pre
        tmp = curr.next
        curr.next = pre
        pre = curr
        return self.reverseRecur(tmp, pre)

