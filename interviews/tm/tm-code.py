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
#   he
#   llow


# result = [hell,ow]

# hell






class Solution():
    words = {"hell", "ow", "worl", "hello", "world","he","llow"}
    

    def split_word(self, string_input: str):
        hit_map = [0] * len(string_input)

        def split_internal(string_input, start):
            if string_input[start:] in self.words:
                return [string_input[start:]] # True

            for pos in range(start, len(string_input)):
                # check word in dict
                if hit_map[pos] == 0 and string_input[start:pos] in self.words:
                    subsplit = split_internal(string_input, pos) # [] ow + split_internal(orld)
                
                    if subsplit:
                        return [string_input[start:pos]] + subsplit
                    else:
                        hit_map[pos] = 1


            return [] # False
        


        return split_internal(string_input, 0)
    


sol = Solution()
result = sol.split_word("helloworld")
print(result)


