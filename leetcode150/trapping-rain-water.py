from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        result = 0
        last_levels = [] # [[level, idx],]

        start = len(height)
        for i, level in enumerate(height):
            if level:
                start = i
                last_levels.append([level,i])
                break

        for i in range(start + 1, len(height)):
            print(last_levels)
            level = height[i]

            if level == last_levels[-1][0]:
                last_levels[-1][1] = i
                continue

            if level < last_levels[-1][0]:
                last_levels.append([level, i])
                continue

            while(len(last_levels) >= 2  and last_levels[-1][0] <= level):
                print("fill start")
                fill_from = last_levels.pop()[0]
                fill_to = min(last_levels[-1][0], level)
                result += (fill_to - fill_from) * (i - last_levels[-1][1] - 1)
                print(result)
                print(last_levels)

            if last_levels[-1][0] <= level:
                last_levels.pop()

            last_levels.append([level, i])

        return result


case1 = [0,1,0,2,1,0,1,3,2,1,2,1]
case2 = [4,2,0,3,2,5]

# print(Solution().trap(case1))
print(Solution().trap(case2))
