class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        max_substr = 0
        h = set()

        l = 0
        for r in range(len(s)):
            while s[r] in h:
                h.remove(s[l])
                l += 1
            
            h.add(s[r])

            max_substr = max(max_substr, r - l + 1)

        return max_substr
