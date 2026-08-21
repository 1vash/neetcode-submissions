class Solution:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        """Decode a single string back into list of strings
        """
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1

            # We assume that len(word) is before "#"
            # and we take this length word is located from i:j
            word_length = int(s[i:j])
            i = j + 1

            word = s[i:i + word_length]
            res.append(word)
            i = i + word_length

        return res
                 