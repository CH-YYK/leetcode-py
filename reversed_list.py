class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def printListFromTailToHead(self, listnode):
        l = []
        while listnode:
            l.append(listnode.val)
            listnode = listnode.next
        return l[::-1]


if __name__ == '__main__':
    A1 = ListNode(1)
    A2 = ListNode(2)
    A3 = ListNode(3)
    A4 = ListNode(4)
    A5 = ListNode(5)

    A1.next = A2
    A2.next = A3
    A3.next = A4
    A4.next = A5

    solution = Solution()
    ans = solution.printListFromTailToHead(A1)
    print(ans)