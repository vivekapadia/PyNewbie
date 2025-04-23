
# Solution 1: (Brute Force)
class Solution:

    # here the list[int] is just type hints only
    # Py is dynamic so, it won't throw a TypeError unless you add explicit type checking
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        if not all(isinstance(n, int) for n in nums):
            raise TypeError('All elements in "nums" must be integers.')

        if not isinstance(target,int):
            raise TypeError("Target must be an integer.")

        n = len(nums)
        for i in range(n-1):
            for j in range(i+1,n):
                if nums[i] + nums[j] == target:
                    return [i,j]
        return [] # No solution found

# Solution 2: (Two-pass Hash Table)
# class Solution:
#     def twoSum(self, nums: list[int], target: int) -> list[int]:
#         numMap = {}
#         n = len(nums)
#
#         # Build the hash table
#         for i in range(n):
#             numMap[nums[i]] = i
#
#         # Find the complement
#         for i in range(n):
#             complement = target - nums[i]
#             if complement in numMap and numMap[complement] != i:
#                 return [i,numMap[complement]]
#
#         return [] # No solution found

# Solution 3: (One-pass Hash Table)
# class Solution:
#
#     def twoSum(self, nums: list[int], target: int) -> list[int]:
#
#         numMap = {}
#         n = len(nums)
#
#         for i in range(n):
#             complement = target - nums[i]
#             if complement in numMap:
#                 return [numMap[complement],i]
#             numMap[nums[i]] = i
#
#         return []

# testcases
sol = Solution()
print(sol.twoSum([2,7,11,15],9))
print(sol.twoSum([3,2,4],7))
print(sol.twoSum([3,3],6))