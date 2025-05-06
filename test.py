class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        found = [False, False]
        for i in range(len(nums)):
            found[0] = i
            placeholder = nums.pop(i)
            left = target - placeholder
            if left in nums:
                nums.insert(i, "p")
                found[1] = nums.index(left)
                nums.remove("p")
                nums.insert(i, placeholder)
                return found
            nums.insert(i, placeholder)
            
    def addNums(self, a, b):
        return a + b
        
problem = Solution()

# Two Sum Test
# nums = list(map(int, input().split()))
# target = int(input())
# print(problem.twoSum(nums, target))

