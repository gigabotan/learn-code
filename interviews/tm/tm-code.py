# we have a string "helloworld"
# we want to segment into separate words
# return: List[str]  ["hello", "world"]
# we have dictionary of words


# dictionary:
#   hell
#   ow
#   worl
#   hello
#   world


# result = [hell,ow]

class Solution():
    words = {""}

    def split_word(self, string_input: str):
        if string_input in self.words:
            return [string_input]

        for pos in range(len(string_input)):
            # check word in dict
            if string_input[:pos] in self.words:
                subsplit = self.split_word(string_input[:pos]) # [], ["fasdf", "fasdf"]
                
            if subsplit:
                return string_input[:pos] + subsplit

        return []





