from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # T: O(2*N), S: O(N~26)
        if len(s) != len(t):
            return False

        h = defaultdict(int) # OR count = [0] * 26
        for char_s, char_t in zip(s, t):
            h[char_s] += 1
            h[char_t] -= 1

        return all(value == 0 for value in h.values())
        
