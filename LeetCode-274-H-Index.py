class Solution:
    def hIndex(self, citations: 'List[int]') -> 'int':
        citations.sort()
        for i in range(len(citations)-1, -1, -1):
            if citations[i] < len(citations) - i:
                return len(citations)-i-1
        return len(citations)
