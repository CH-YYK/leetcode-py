class Solution:
    def groupAnagrams(self, strs: 'List[str]') -> 'List[List[str]]':
        hashmap = {}
        for i in strs:
            tmp = ''.join(sorted(i))
            if tmp in hashmap:
                hashmap[tmp].append(i)
            else:
                hashmap[tmp] = [i]
        return [i for i in hashmap.values()]

if __name__ == "__main__":
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(Solution().groupAnagrams(strs))