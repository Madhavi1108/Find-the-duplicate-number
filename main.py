class Solution(object):
    def findDuplicate(self, nums):
        for i in range(0,len(nums)):
            count = 0
            for j in range(0, len(nums)):
                if nums[i] == nums[j]:
                    count += 1

            if count > 1:
                return nums[i]
                break


a = input().split()
nums = [int(i) for i in a]
solution = Solution()
ans = solution.findDuplicate(nums)
print(ans)
