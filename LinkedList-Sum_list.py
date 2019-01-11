"""
Two numbers represented by a linked list, where each node contains a single digit.
The digits are stored in reverse order, such as (7-1-6) := 617
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def sumList(self, node1, node2):
        return self.recursiveSum(node1, node2, 0)

    def recursiveSum(self, node1, node2, carry):
        if node1 is None and node2 is None and carry == 0:
            return None

        result = ListNode(None)
        value = carry

        if node1:
            value += node1.val
        if node2:
            value += node2.val

        result.val = value % 10
        carry = value // 10
        result.next = self.recursiveSum(node1.next if node1 else None,
                                        node2.next if node2 else None,
                                        carry)
        return result

if __name__ == '__main__':
    n1_1 = ListNode(6)
    n1_2 = ListNode(1)
    n1_3 = ListNode(7)

    n2_1 = ListNode(5)
    n2_2 = ListNode(9)
    n2_3 = ListNode(2)

    n1_1.next = n1_2
    n1_2.next = n1_3

    n2_1.next = n2_2
    # n2_2.next = n2_3

    ans = Solution().sumList(n1_1, n2_1)