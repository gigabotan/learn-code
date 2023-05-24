# https://leetcode.com/problems/word-break
import typing

class Solution:

    # Solution without recursion
    # 
    # def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    #     dp = [False] * (len(s) + 1)
    #     dp[0] = True
    #     for i in range(0, len(s)):
    #         for j in range(i, -1, -1):
    #             if dp[j] and (s[j:i + 1] in wordDict):
    #                 dp[i + 1] = True
    #                 break
    #     return dp[len(s)]




    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        hit_map = [0] * len(s)

        def split_internal(s, start):
            if s[start:] in wordDict:
                return True

            for pos in range(start, len(s)):
                # check word in dict
                if hit_map[pos] == 0 and s[start:pos] in wordDict:
                    subsplit = split_internal(s, pos) #
                
                    if subsplit:
                        return True
                    else:
                        hit_map[pos] = 1

            return False


        return split_internal(s, 0)