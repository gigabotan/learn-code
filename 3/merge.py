class Solution:
    def merge(self, left, right):
        sorted_list = []
        left_pos = 0
        right_pos = 0
        
        while(left_pos < len(left) and right_pos < len(right)):
            
            if left[left_pos] < right[right_pos]:
                sorted_list.append(left[left_pos])
                left_pos += 1
            else:
                sorted_list.append(right[right_pos])
                right_pos += 1

        if left_pos == len(left):
            sorted_list.extend(right[right_pos:])
        else:
            sorted_list.extend(left[left_pos:])
            
        return sorted_list


    def mergesort(self, heights):
        if len(heights) <= 1:
            return heights

        center = len(heights) // 2

        left = self.mergesort(heights[:center])
        right = self.mergesort(heights[center:])

        heights = self.merge(left, right)

        return heights


# heights = [1,1,4,2,1,3]
# heights = [5,1,2,3,4]
# heights = [1,2,3,4,5]
heights = []


a = Solution()
result = a.mergesort(heights)
print(result)





