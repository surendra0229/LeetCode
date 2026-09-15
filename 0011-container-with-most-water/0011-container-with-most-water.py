class Solution(object):
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        max = 0
        
        while left < right:
            currentWater = (right - left) * min(height[left], height[right])
            if currentWater > max :
                max = currentWater
                
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return max
        