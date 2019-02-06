class Solution:
    def all_subsets(self, array):
        all_subset = []
        self.getsubsets(array, [], index=0, all_subset=all_subset)
        return all_subset

    def getsubsets(self, array, subset, index, all_subset):
        if index == len(array):
            all_subset.append([i for i in subset if i])
            return
        else:
            self.getsubsets(array, subset+[None], index+1, all_subset)
            self.getsubsets(array, subset+[array[index]], index+1, all_subset)

if __name__ == '__main__':
    print(Solution().all_subsets([1,2]))