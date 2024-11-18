class Solution(object):
    def findDuplicate(self, nums):
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)
a = input().split()
nums = [int(i) for i in a]
solution = Solution()
ans = solution.findDuplicate(nums)
print(ans)
