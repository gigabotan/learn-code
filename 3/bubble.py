class Solution:
    def heightChecker(self, heights):
        
        for i in range(len(heights) - 1):
            already_sorted = True
            for j in range(len(heights)-1):
                if heights[j] > heights[j+1]:
                    heights[j], heights[j+1] = heights[j+1], heights[j]
                    already_sorted = False
            if already_sorted:
                break                    
        return heights


# heights = [1,1,4,2,1,3]
# heights = [5,1,2,3,4]
heights = [1,2,3,4,5]


a = Solution()
result = a.heightChecker(heights)
print(result)