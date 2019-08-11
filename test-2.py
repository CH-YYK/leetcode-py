def helper(num):
    str_num = bin(num)[2:]
    i = 0
    num = 0
    while i < len(str_num) - 1:
        if str_num[i:i+1] == '10':
            i += 2
            if str_num[i] == '1':
                num += 1
        else:
            i += 1
    return num

def fun(R, K):
    res = [0] * R
    for i in range(R):
        curr = i + 1
        if res[i] == 0:
            res[i] = helper(curr)
        while curr <= R and res[curr-1] == 0:
            tmp = res[curr-1]
            if curr & 1:
                curr <<= 2
                curr += 1
                res[curr-1] = tmp + 1
            elif curr & 2:
                curr << 1
                curr += 1
                res[curr-1] = tmp + 1
            else:
                break
    return sum([1 for i in res if i >= K])
                
            

if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        R, K = [int(i) for i in input().split()]
        print(fun(R, K))

    print(helper(5))