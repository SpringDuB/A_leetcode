class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        if len(strs) in [0, 1]:
            return [strs]
        resu = []
        dic = {}
        for str1 in strs:
            temp = ''.join(sorted(str1))
            if temp in dic:
                dic[temp].append(str1)
            else:
                dic[temp] = [str1]
        return list(dic.values())


                



if __name__ == '__main__':
    str = ["eat", "tea", "tan", "ate", "nat", "bat"]
    solution = Solution()
    res = solution.groupAnagrams(str)
    print(res)