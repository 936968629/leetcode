class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # [l, ... , r]滑动窗口
        l = 0
        r = -1
        # 定义为最小
        res = 0
        countList = {}

        # while l < len(s):
        #     if s[r+1] in countList.keys()  and r + 1 < len(s):
        #         r += 1
        #         # countList[s[r]] = 1
        #     else:
        #         countList[s[r]] = 1
        #         l += 1


        # print(countList)
        # return res


        cache = {}
        longest = 0
        start = 0
        for i,v in enumerate(s):
            if v in cache:
                start = max(start, cache[v]+1)
            cache[v] = i
            longest = max(longest, i-start+1)
        return longest

str = 'bba'
Sol = Solution()
Sol.lengthOfLongestSubstring(str)
