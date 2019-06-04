
def unboundedKnapsack(k, arr):
    def helper(k, arr, memo):
        if k in arr:
            return k
        if k in memo:
            return memo[k]
        val = 0
        for ele in arr:
            if ele > k:
                continue
            val = max(val, ele + helper(k-ele, arr, memo))
        memo[k] = val
        return memo[k]
    return helper(k , arr, {})

def unboundedKnapsack2(k, arr):
    val = 0
    dp = [0 for i in range(k+1)]
    queue = [val]
    while queue:
        size = len(queue)
        while size > 0:
            curr = queue.pop(0)
            for i in arr:
                if curr + i > k or dp[curr+i] > 0:
                    continue
                queue.append(i + curr)
                dp[i + curr] = 1
            size -= 1
    for i in range(k, 0, -1):
        if dp[i] > 0:
            return i
    return 0

def unboundedKnapsack3(k, arr):
    dp = [0 for _ in range(k+1)] # maximum sum under i
    for i in range(1, k+1):
        for ele in arr:
            if ele > i:
                continue
            dp[i] = max(dp[i], dp[i - ele] + ele)
    return dp[k]


if __name__ == "__main__":
    arr = [2000, 2000, 2000]
    n = 3
    k = 2000

    # print(unboundedKnapsack3(k , arr))

    t = int(input())

    for i in range(t):
        n, k = input().split()
        arr = [int(i) for i in input().split()]
        print(unboundedKnapsack2(int(k), arr))