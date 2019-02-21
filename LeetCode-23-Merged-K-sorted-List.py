import sys, heapq
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists: 'List[ListNode]') -> 'ListNode':
        """
        O(n*k*log(nk)) in time, O(nk) in space
        """
        if not lists:
            return None
        nodes = []
        for head in lists:
            while head:
                nodes.append(head.val)
                head = head.next

        nodes.sort()

        newList = ListNode(0)
        curr = newList
        for node in nodes:
            curr.next = ListNode(node)
            curr = curr.next
        return newList.next

    def mergeKLists2(self, lists: 'List[ListNode]') -> 'ListNode':
        """
        O(nk^2) in time, O(1) in space
        """
        newList = ListNode(0)
        curr = newList

        while True:
            index, minHeadVal = None, sys.maxsize
            for i, head in enumerate(lists):
                if head and head.val < minHeadVal:
                    minHeadVal = head.val
                    index = i
            if minHeadVal == sys.maxsize:
                break
            lists[index] = lists[index].next
            curr.next = ListNode(minHeadVal)
            curr = curr.next
        return newList.next

    def mergeKLists3(self, lists: 'List[ListNode]') -> 'ListNode':
        """
        O(n*k*log(k)) in time, O(1) in space, with heap
        """
        if not lists or not lists[0]:
            return None
        newList = ListNode(0)
        curr = newList

        # build heap
        heap = []
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i], i))
                lists[i] = lists[i].next

        while heap:
            headVal, index = heapq.heappop(heap)
            if lists[index]:
                heapq.heappush(heap, (lists[index].val, index))
                lists[index] = lists[index].next
            curr.next = ListNode(headVal)
            curr = curr.next
        return newList.next

