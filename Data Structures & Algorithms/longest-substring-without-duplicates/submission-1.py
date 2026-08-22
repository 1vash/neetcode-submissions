class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # T: O(N); S: O(N)
        l = longest_s = 0
        h = set()

        for r in range(len(s)):
            while s[r] in h:
                h.remove(s[l])
                l += 1

            longest_s = max(r - l + 1, longest_s)
            h.add(s[r])

        return longest_s