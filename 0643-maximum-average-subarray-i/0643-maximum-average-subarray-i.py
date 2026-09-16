class Solution:
    def findMaxAverage(self, nums, k):
        left = 0
        sum = 0
        maximum = float("-inf")
        for right in range(len(nums)):
            sum += nums[right]
            if right - left + 1 == k:
                maximum = max(maximum, sum)
                sum -= nums[left]
                left += 1
        return maximum/k