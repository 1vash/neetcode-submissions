from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        # 26 uppercase characters, worst case
        h = defaultdict(int)

        ans = 0

        l = 0
        for r in range(len(s)):
            h[s[r]] += 1
            most_frequent_val = sorted(h.values(), reverse=True)[0]
            len_substr = r - l + 1
            n_all_replacements = len_substr - most_frequent_val
            while n_all_replacements > k:
                h[s[l]] -= 1
                if h[s[l]] == 0:
                    del h[s[l]]
                l += 1
                len_substr = r - l + 1
                n_all_replacements = len_substr - most_frequent_val

            most_frequent_with_replacements = most_frequent_val + min(n_all_replacements, k)
            ans = max(most_frequent_with_replacements, ans)

        return ans