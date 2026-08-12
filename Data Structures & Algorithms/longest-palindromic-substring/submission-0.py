class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        res = ""
        res_len = 0
        
        def expand(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            # return palindrome length and substring
            return s[l+1:r]
        
        for i in range(len(s)):
            # odd length palindrome
            p1 = expand(i, i)
            if len(p1) > res_len:
                res = p1
                res_len = len(p1)
            
            # even length palindrome
            p2 = expand(i, i+1)
            if len(p2) > res_len:
                res = p2
                res_len = len(p2)
        
        return res

        