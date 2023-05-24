# https://leetcode.com/problems/word-break-ii/
import typing

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:

        dp = [[]] * (len(s) + 1)
        dp[0] = [0]

        for i in range(0, len(s)):
            for j in range(i, -1, -1):
                if dp[j] and (s[j:i + 1] in wordDict):
                    dp[i + 1].append(j)
                    break

        # TODO: finish dfs words combine

        return []

    def combine(self, dp_list, s, pos):
        pass
        