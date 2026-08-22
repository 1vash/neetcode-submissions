# length before special symbol
# ["hello", "my", "name"]
# 5@hello2@my4@name

class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for s in strs:
            encoded_string += str(len(s)) + "@" + s
        return encoded_string

    def decode(self, s: str) -> List[str]:
        i, j = 0, 0
        decoded_list = []
        while i < len(s) and j < len(s):

            while j < len(s) and s[j] != "@":
                j += 1

            if j > len(s):
                break

            length = int(s[i:j])
            
            word_start = j + 1
            word_end = word_start + length
            
            decoded_str = s[word_start:word_end]
            decoded_list.append(decoded_str)

            i = word_end
            j = i + 1

        
        return decoded_list
         


            
