# Given a collection of numbers that might contain duplicates, return all possible unique permutations.

class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return []
        visited = [False] * len(nums)
        results = []
        nums.sort()
        
        def findPermute(nums, visited, curr, results):
            if len(curr) == len(nums):
                results.append(curr)
                return 
            i = 0
            while i < len(nums):
                if visited[i] == False:
                    visited[i] = True
                    findPermute(nums, visited, curr+[nums[i]], results)
                    visited[i] = False
                    while(i < len(nums)-1 and nums[i]==nums[i+1]):
                        i += 1
                i += 1
        findPermute(nums, visited, [], results)
        return results
                    
        
