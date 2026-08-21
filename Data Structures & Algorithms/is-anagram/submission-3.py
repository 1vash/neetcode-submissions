class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars = [0] * 26

        for char in s:
            chars[ord(char) - 97] += 1

        for char in t:
            chars[ord(char) - 97] -= 1

        return all(x == 0 for x in chars)
