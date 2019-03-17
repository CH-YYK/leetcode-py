class comp:
    def __init__(self, x):
        self.x = x
    
    def __lt__(self, other):
        return self.comp(self.x, other.x)
    
    def comp(self, idea1, idea2):
        if idea1[2] != idea2[2]:
            return idea1[2] > idea2[2]
        
        if idea1[3] != idea2[3]:
            return idea1[3] < idea2[3]
        
        if idea1[1] != idea2[1]:
            return idea1[1] < idea2[1]

class comp2:
    def __init__(self, x):
        self.x = x

    def __lt__(self, other):
        return self.comp(self.x, other.x)
    
    def comp(self, idea1, idea2):
        if idea1[3] != idea2[3]:
            return idea1[3] < idea2[3]
        return idea1[0] < idea2[0]

class Solution(object):
    def returnTime(self, nums, n, m, p):
        hashmap = {}
        
        # add index to ideas
        for i, j in enumerate(nums):
            j.append(i)
        
        # assign ideas to each PM
        for i in nums:
            hashmap[i[0]] = hashmap.get(i[0], []) + [i]
        
        # rank each ideas for each PM
        for i in hashmap:
            hashmap[i] = sorted(hashmap[i], key=comp)
        
        # 
        pendingcase = []
        lis = []
        while True:
            for i in hashmap:
                lis += [hashmap[i].pop(0)] if hashmap[i] else []
            if not lis: break
            lis =  sorted(lis, key = comp2)
            pendingcase.append(lis.pop(0))
        print(pendingcase)

        # result
        res = [0] * len(pendingcase)

        # programmer
        programmer = [0] * m

        # 
        i = 0
        while pendingcase:
            case = pendingcase.pop(0)
            programmer[i] += case[3]
            res[case[4]] = programmer[i]
            i += 1
            i %= m
        return res

if __name__ == "__main__":
    nums = [[1, 1, 1, 2],
            [1, 2, 1, 1],
            [1, 3, 2, 2],
            [2, 1, 1, 2],
            [2, 3, 5, 5]]
    ans = Solution().returnTime(nums, 2,2,5)
    print(ans)