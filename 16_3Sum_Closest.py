# Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. 
# Return the sum of the three integers. You may assume that each input would have exactly one solution.

class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        def findNSum(nums, N, target):
            if N == 2:
                start, end = 0, len(nums)-1
                best = nums[start]+nums[end]
                while start < end:
                    Sum = nums[start]+nums[end]
                    if Sum == target:
                        best = Sum
                        return best
                    elif Sum < target:
                        start += 1
                    else:
                        end -= 1
                    if abs(target-Sum) < abs(target-best):
                        best = Sum
                return best
            else:
                best = sum(nums[0:3])
                for i in range(len(nums)-2):
                    Sum = nums[i] + findNSum(nums[i+1:], N-1, target-nums[i])
                    if abs(target-Sum) < abs(target-best):
                        best = Sum
            return best
        
        nums.sort()
        return findNSum(nums, 3, target)
                
