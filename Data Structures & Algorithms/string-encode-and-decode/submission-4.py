class Solution:
    num_length = 3
    def num_to_string(self, val: int) -> str:
        return_string = str(val)
        length_diff = len(return_string) - self.num_length 
        while length_diff < 0: 
            return_string = "0" + return_string
            length_diff += 1
        return return_string
    def encode(self, strs: List[str]) -> str:
        return_string = self.num_to_string( len(strs) )
        for string in strs:
            return_string += self.num_to_string(len(string))
        for string in strs:
            return_string += string
        return return_string
    def decode(self, s: str) -> List[str]:
        n_elements = int(s[0:self.num_length])
        s = s[self.num_length:len(s)]
        i = 0
        j = n_elements*self.num_length
        decoded_elements = []
        while (i < n_elements*self.num_length):
            string_length = int(s[i:i+self.num_length]) 
            element = s[j:j+string_length]
            decoded_elements.append(element)
            j += string_length
            i += self.num_length
        return decoded_elements

