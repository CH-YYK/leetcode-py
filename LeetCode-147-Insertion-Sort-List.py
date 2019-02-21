import sys
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def insertionSortList(self, head: 'ListNode') -> 'ListNode':
        if not head: return head

        newList = ListNode(-sys.maxsize)
        curr = newList
        while head:
            if head.val > curr.val:
                curr.next = head
                head = head.next
                curr = curr.next
                curr.next = None
            else:
                newcurr = newList
                while newcurr.next and newcurr.next.val < head.val:
                    newcurr = newcurr.next
                tmp = newcurr.next
                newcurr.next = head
                head = head.next
                newcurr.next.next = tmp
        return newList.next

if __name__ == '__main__':
    head = ListNode(4)
    head.next = ListNode(3)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(1)
    ans = Solution().insertionSortList(head)
    while ans:
        print(ans.val)
        ans = ans.next
