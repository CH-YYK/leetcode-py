def minpalindrome(string):
    chars = [0 for _ in range(26)] 
    num_odd = 0
    for ch in string:
        chars[ord(ch) - ord('a')] += 1
    for i in chars:
        num_odd += (i % 2 > 0)
    return num_odd

if __name__ == "__main__":
    string = input()
    print(minpalindrome(string))