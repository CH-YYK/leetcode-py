class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    # two pointers
    def middle_element_list(self, head):
        current = head
        middle = head
        length = 0
        while current.next:
            length += 1
            current = current.next
            if length % 2 == 0:
                middle = middle.next
        return middle.val


if __name__ == '__main__':
    p1 = ListNode(1)
    p2 = ListNode(2)
    p3 = ListNode(3)
    p4 = ListNode(4)
    p5 = ListNode(5)

    p1.next = p2
    p2.next = p3
    p3.next = p4
    p4.next = p5

    print(Solution().middle_element_list(p1))
