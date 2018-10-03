class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # find_map = {}
        # returnData = []
        # for item in strs:
        #     sortedStr = ''.join(sorted(item))
        #     if sortedStr in find_map.keys():
        #         find_map[sortedStr].append(item)
        #     else:
        #         find_map[sortedStr] = [item]
        # for k, v in find_map.items():
        #     returnData.append(v)
        # print(returnData)
        # return returnData
        find_map = {}
        # returnData = []
        for item in strs:
            sortedStr = ''.join(sorted(item))
            if sortedStr in find_map.keys():
                find_map[sortedStr].append(item)
            else:
                find_map[sortedStr] = [item]
        return list(find_map.values())


parstrs = ["eat", "tea", "tan", "ate", "nat", "bat"]
sol = Solution()
sol.groupAnagrams(parstrs)