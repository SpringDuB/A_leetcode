class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in nums:
            temp = nums.copy()
            temp.remove(i)
            if target - i in temp:
                j = target - i
                return [nums.index(i), nums.index(j)]

if __name__ == "__main__":
    nums = [3, 2, 4]
    target = 7
    sol = Solution()
    res = sol.twoSum(nums, target)
    print(res)