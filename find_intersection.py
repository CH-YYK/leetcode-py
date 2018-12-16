class Solution:
    def findIntersection(self, array1, array2, array3):
        result = []
        x = y = z = 0
        while x < len(array1) and y < len(array2) and z < len(array3):
            if array1[x] == array2[y] and array2[y] == array3[z]:
                result.append(array1[x])
                x += 1
                y += 1
                z += 1
            elif array1[x] < array2[y]:
                x += 1
            elif array2[y] < array3[z]:
                y += 1
            else:
                z += 1
        return result

if __name__ == '__main__':
    array1 = [2, 6, 9, 11, 13, 17]
    array2 = [3, 6, 7, 10, 13, 18]
    array3 = [4, 5, 6, 9, 11, 13]

    print(Solution().findIntersection(array1, array2, array3))