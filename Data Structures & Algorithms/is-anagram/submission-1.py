class Solution:
    def isAnagram(self, s: str, t: str) -> bool:        
        if len(s) != len(t):
            return False

        # possible to use ASCII 26 letter table instead of dict
        chars_s = defaultdict(int)
        chars_t = defaultdict(int)

        for char in s:
            chars_s[char] += 1

        for char in t:
            chars_t[char] += 1

        # Check if the character counts are equal for both strings
        return all(chars_t[char] == count for char, count in chars_s.items())
