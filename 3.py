class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # [l, ... , r]滑动窗口
        l = 0
        r = -1
        res = 0
        countList = {0} * 200

        # while l < len(s):
        #     if countList.has_key(s [r+1])   and r + 1 < len(s):
        #         r += 1
        #
        #     else:
        #         # newlist.remove(s[l])
        #         l = r
        #         l += 1

        print(countList[s[r+1]])
        # print(res)
        return res


str = 'bba'
Sol = Solution()
Sol.lengthOfLongestSubstring(str)
