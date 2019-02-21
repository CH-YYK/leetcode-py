# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution(object):
    def copyRandomList(self, head):
        """
        O(N) in time, O(N) in space
        """
        if not head:
            return None
        newNode = RandomListNode(0)
        prev = newNode
        hashmap = {}
        while head:
            if head not in hashmap:
                hashmap[head] = RandomListNode(head.label)
            prev.next = hashmap[head]
            if head.random:
                hashmap[head.random] = RandomListNode(head.random.label)
                prev.next.random = hashmap[head.random]
            prev = prev.next
            head = head.next
        return newNode.next

    def copyRandomList2(self, head):
        """
        O(N) in time, O(1) in space
        """
        if not head:
            return None
        headCopy = head
        while headCopy:
            nodeCopy = RandomListNode(headCopy.label)
            nodeCopy.next = headCopy.next
            headCopy.next = nodeCopy
            headCopy = headCopy.next.next

        headCopy = head
        while headCopy:
            nodeCopy = headCopy.next
            if headCopy.random:
                nodeCopy.random = headCopy.random.next
            headCopy = headCopy.next.next

        newNode = RandomListNode(0)
        nodeCopy = newNode
        curr = head
        while curr:
            nodeCopy.next = curr.next
            curr.next = curr.next.next
            nodeCopy = nodeCopy.next
            curr = curr.next
        return newNode.next



