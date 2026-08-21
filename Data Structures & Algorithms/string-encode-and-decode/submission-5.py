class Solution:
    symbol = "#"

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for s in strs:
            length_num = len(s)
            new_s = str(length_num) + self.symbol + s 
            encoded.append(new_s)
        return "".join(encoded) # appending strings is not optimal as string is immutable and we in the loop alway do copying
            

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        # find the '#'
        while i < len(s):
            j = i
            
            while s[j] != self.symbol:
                j += 1            
            length = int(s[i:j])
            start = j + 1 # skip special symbol
            end = start + length  # length starts from 1-th idx, which means that s[:length] covers the right border of slicing correctly
            decoded.append(s[start:end])
            
            i = end
        
        # j = i and i = end creates a perfect loop

        return decoded
        


        




# Tests: 
#  ["neet","c#o3de","love","you"]
# Encode: ["4#neet", "6#c#o3de", "4#lvoe", "3#you"]
# start Decoding since 1st of element = which is number assigned by us followed by "#"3a