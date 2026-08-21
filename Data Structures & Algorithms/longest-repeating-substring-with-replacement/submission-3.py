class Solution:
    # Solution: Sliding window counts WINDOW'S ALL characters and keeps track of the most frequent one.
    # Shrink from the left only when replacements needed exceed k.

    # T: O(N); S: O(M) ~ m total num of unique chars in the string
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        count = defaultdict(int)        
        max_window = 0
        max_freq_char = 0

        for r in range(len(s)):

            count[s[r]] += 1
            # we increased only s[r], validate with max_freq only this one
            max_freq_char = max(count[s[r]], max_freq_char)

            while (r - l + 1) - max_freq_char > k:
                count[s[l]] -= 1
                l += 1
 
            max_window = max(r - l + 1, max_window)

        return max_window