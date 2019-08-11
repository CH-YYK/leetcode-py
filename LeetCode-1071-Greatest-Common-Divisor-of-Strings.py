class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        """
        assume len(str2) < len(str1), str2 should be one substring of str1
        """
        return self.helper(str1, str2) if len(str1) <= len(str2) else self.helper(str2, str1)
            

    def helper(self, str_s, str_l):
        if len(str_s) == len(str_l):
            return str_s if str_s == str_l else ""
        
        for i in range(len(str_s)):
            if str_s[i] != str_l[i]:
                return ""
        str_l = str_l[i+1:]
        if len(str_s) < len(str_l):
            return self.helper(str_s, str_l)
        return self.helper(str_l, str_s)

class Solution2:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        """
        assume len(str2) < len(str1), str2 should be one substring of str1
        """
        return self.helper(str1,0, str2,0) if len(str1) <= len(str2) else self.helper(str2,0, str1,0)
            

    def helper(self, str_s, i_s, str_l, i_l):
        if len(str_s) - i_s == len(str_l) - i_l:
            return str_s[i_s:] if str_s[i_s:] == str_l[i_l:] else ""
        
        for i in range(i_s, len(str_s)):
            if str_s[i] != str_l[i_l + i - i_s]:
                return ""

        i_l += len(str_s) - i_s

        if len(str_s) - i_s < len(str_l) - i_l:
            return self.helper(str_s, i_s, str_l, i_l)
        return self.helper(str_l, i_l, str_s, i_s)


if __name__ == "__main__":
    str1 = 'ABABAB'
    str2 = 'ABAB'
    print(Solution2().gcdOfStrings(str1, str2))
 