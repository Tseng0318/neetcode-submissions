class Solution:

# Position: 0 1 2 3 4 5 6 7 8 9 10 11
# Char:     4 # l i n t 4 # c o  d  e

    def encode(self, strs: List[str]) -> str:
        string = ""
        for items in strs:
            string = string + str(len(items))+ "#" + items
        return string

    def decode(self, s: str) -> List[str]:
        i = 0
        result = []
        while i < len(s):
            j = s.find("#", i)
            length = int(s[i:j])
            word = s[j+1:j+length+1]
            result.append(word)
            i = length + j +1
        return result


