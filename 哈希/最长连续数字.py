class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if len(nums) in [0, 1]:
            return len(nums)
        nums.sort()
        l = 0
        max = 0
        for i in range(len(nums)-1):
            if nums[i+1] == nums[i] and i < len(nums) -2:
                continue
            if abs(nums[i+1] - nums[i]) == 1:
                l += 1
            else:
                 if l > max :
                     max=l
                 l = 0
            if i == (len(nums) - 2) and l > max:
                max = l
        return max+1
    
if __name__ == "__main__":
    nums =[1]
    a = Solution()
    res = a.longestConsecutive(nums)
    print(res)