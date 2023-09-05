class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l1 = len(nums)
        while 1:
            if 0 in nums:
                nums.remove(0)
            else:
                break
        l2 = len(nums)
        for i in range(l1-l2):
            nums.append(0)
    

if __name__ =="__main__":
    nums = [0,0,0,0,0,0,1,1,1]
    a = Solution()
    res = a.moveZeroes(nums)
    print(res)