class Solution:
    # def reverseString(self, s):
    #     """
    #     Do not return anything, modify s in-place instead.
    #     """
    #     start = 0
    #     end = len(s) - 1
    #     while(start < end):
    #         s[start], s[end] = s[end], s[start]
    #         start += 1
    #         end -= 1

    # def reverseString(self, s):
    #     s[:] = s[::-1]

    def reverseString(self, s):
        s.reverse()


s = ["h","e","l","l","o"]
sol = Solution()
sol.reverseString(s)