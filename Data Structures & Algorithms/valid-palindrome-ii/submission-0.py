class Solution:
    # T: O(2N)~O(N), S: O(1)
    def is_palindrome(self, s, e):
        while s < e:
            if self.s[s] != self.s[e]:
                return False
            s += 1
            e -= 1
        return True

    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) -1 
        self.s = s
        while l < r:
            if self.s[l] != self.s[r]:
                return self.is_palindrome(l+1, r) or self.is_palindrome(l, r-1)
            l += 1
            r -= 1
        return True