def maxDNA(string):
    # A T C G
    chars = [0 for _ in range(26)]
    lft = 0
    rht = 0
    maxlen = 0
    while rht < len(string):
        if string[rht] not in ['A', 'T', 'C', 'G']:
            maxlen = max(maxlen, rht - lft)
            lft = rht + 1
        rht += 1
    return max(maxlen, rht - lft)

if __name__ == "__main__":
    string = input()
    print(maxDNA(string))