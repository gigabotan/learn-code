# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s):
        start = 0
        end = 0
        max_len = 0

        chars = {}

        while(end < len(s)):
            if (s[end] not in chars.keys()):
                chars[s[end]] = end
                end += 1
                cur_len = end - start
                if cur_len > max_len: max_len = cur_len
                continue

            cut_end = chars[s[end]]

            while(start <= cut_end):
                chars.pop(s[start])
                start += 1

        return max_len



s = "abcabcbb"
result = 3

sol = Solution()
result = sol.lengthOfLongestSubstring(s)
print(result)