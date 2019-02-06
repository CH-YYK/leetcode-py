import heapq


class Solution:
    def findMinimumPowerforKmachines(self, N, K):

        # compute ratios and order N wrt ratios in descending order
        newSet = []
        for machine in N:
            ratio = machine[0] / machine[1]
            # create new tuple for each machine (negative speed, leastPower, computed ratio)
            newSet.append((-machine[0], machine[1], ratio))
        newSet.sort(key=lambda x: -x[-1])

        # select first K machines as base subset and build maxheap of speed.
        # == minHeap of negative speed.
        subset = newSet[:K]
        heapq.heapify(subset)

        # compute the miniPower with currRatio
        currRatio = subset[-1][2]
        currMini = sum([-i[0] for i in subset])/currRatio

        # test from (K+1)th machine in ordered set. compare its speed with the max speed in Heap
        for i in range(K, len(newSet)):
            # if new speed is greater --> compute new minPower and compare
            if newSet[i][0] < subset[0][0]:
                newMini = (currMini * currRatio + subset[0][0] - newSet[i][0])/newSet[i][2]
                if newMini <= currMini:
                    heapq.heapreplace(subset, newSet[i][0])
                    currMini = newMini
                    currRatio = newSet[i][2]
        # O(N) + O(Nlog(N)) + O(log(K)) + O((N-K)log(K)) = O(N(1+log(N))+(N-K+1)log(K))
        return currMini, currRatio, subset

if __name__ == '__main__':
    N = [(3, 1), (4, 1), (5, 1)]
    K = 2
    ans = Solution().findMinimumPowerforKmachines(N, K)
    print(ans)