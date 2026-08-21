class Solution:
    # The idea: Encode any word, add length and special symbol. e.g 4#neet4#code4#love4#you 
    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for word in strs:
            encoded += str(len(word)) + "#" + word
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []

        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1

            # We assume that len(word) is before "#"
            # and we take this length word is located from i:j
            word_length = int(s[i:j])
            i = j + 1 # skip #

            word = s[i: i + word_length]
            decoded.append(word)
            i = i + word_length

        return decoded

"""
Debug:
s = 4#neet4#code4#love4#you 
i = 2
j = 1
word_length = 4
word = s[i:j] = s[2:2+4] = neet
""" 

