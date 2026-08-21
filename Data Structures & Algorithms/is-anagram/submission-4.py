class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        ascii_arr = [0] * 26
        for char_s, char_t in zip(s, t):
            ascii_arr[ord(char_s) - 97] += 1
            ascii_arr[ord(char_t) - 97] -= 1        

        return all(i == 0 for i in ascii_arr)