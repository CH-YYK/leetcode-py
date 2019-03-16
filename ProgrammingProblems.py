import time
import random

st = time.clock()
class Solution:
    def spiralMemory(self, num):
        # compute minimum number of periods to cover before reaching 1
        if num <= 3:
            return num - 1
        n = 0
        while (2 * n + 1) ** 2 <= num:
            n += 1
        
        # compute distance to nearest local center
        i = 0
        while (2 * n + 1) ** 2 - i * (2*n) >= num:
            i += 1
        
        # return the sum of two segments
        return abs((2*n + 1) ** 2 - (2*i-1)*(2 * n) // 2 - num) + n

    def findingNumber(self, num):
        res = []
        # reduce num by dividing it by 5 or 3 or 2 until 1
        while num > 1:
            if num % 5 == 0:
                res.append(5)
                num //= 5
            elif num % 3 == 0:
                res.append(3)
                num //= 3
            elif num % 2 == 0:
                res.append(2)
                num //= 2
            else:
                return None
        return res[::-1]
    
    def sentenceGenerator(self, sentence):
        # input grammer
        article = ["一个", "这个"]
        none = ["女人","篮子","桌球","小猫"]
        verb = ["看着","听着", "听见"]
        adj = ["","蓝色的","好看的","小小的","年轻的"]

        # simulating words without replacement
        none_selected = random.choices(none, k=2)
        article_selected = random.choices(article, k=2)
        adj_selected = random.choices(adj, k=2)
        verb = random.choice(verb) 

        # none_phrase 1
        none_phrase1 = article_selected.pop() + adj_selected.pop() + none_selected.pop()

        # none_phrase 2
        none_phrase2 = article_selected.pop() + adj_selected.pop() + none_selected.pop()

        # verb : verb
        # construct random sentence
        return " ".join(none_phrase1 + verb + none_phrase2)

    
if __name__ == "__main__":
    # Problem 1
    # Test case1: 1
    print(Solution().spiralMemory(1))
    # Test case1: 12
    print(Solution().spiralMemory(12))
    # Test case1: 23
    print(Solution().spiralMemory(23))
    # Test case1: 1024
    print(Solution().spiralMemory(1024))
    # Test case1: 100000
    print(Solution().spiralMemory(100000))
    # Test case1: 2345678
    print(Solution().spiralMemory(2345678))
    st2 = time.clock()
    print("Time: ", (st2 - st)*1000, " ms")

    # Problem 2
    # Test case2 : 6
    print(Solution().findingNumber(6))
    # Test case2 : 8
    print(Solution().findingNumber(8))
    # Test case2 : 14
    print(Solution().findingNumber(14))
    # Test case2 : 1845281250
    print(Solution().findingNumber(1845281250))
    # Test case2 : 3690562500
    print(Solution().findingNumber(3690562500))
    # Test case2 : 1230187500
    print(Solution().findingNumber(1230187500))
    # Test case2 : 1002357
    print(Solution().findingNumber(1002357))
    st3 = time.clock()
    print("Time : ", (st3 - st2) * 1000, " ms")

    print(Solution().sentenceGenerator('sentence'))