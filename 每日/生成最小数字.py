class Solution:
    def minNumber(self, nums1: list[int], nums2: list[int]) -> int:
        minnum=10
        for i in nums1:
            if i in nums2 and i < minnum:
                minnum=i
        if minnum!=10:
            return minnum
        return min(min(nums1)*10+min(nums2), min(nums2)*10+min(nums1))
        # nums1.sort()
        # nums2.sort()

        # if nums1[0] == nums2[0]:
        #     return nums1[0]
        # else:
        #     if nums1[0] < nums2[0]:

        #         return nums1[0] * 10 + nums2[0]
        #     else:
        #         return nums2[0] * 10 + nums1[0]
        
        


if __name__ == '__main__':
    nums1 = [6, 7, 4]
    nums2 = [3, 6, 2]
    a = Solution()
    res = a.minNumber(nums1, nums2)
    print(res)