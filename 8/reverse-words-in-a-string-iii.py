class Solution:
    def reverseWords(self, s):

        words = s.split(' ')

        words = [word[::-1] for word in words]

        ' '.join(words)



s = "Let's take LeetCode contest"
sol = Solution()
sol.reverseWords(s)