class Solution:
    def trap(self, nums, target):
        if len(nums) == 0:
            return False
        maxnum = 0
        newdict = {}
        for item in numA:
            if not str(item).isdigit():
                aa, bb = item.split('-')
                aa, bb = int(aa), int(bb)
                maxnum = max(maxnum, aa, bb)
                while int(aa) <= int(bb):
                    newdict[aa] = 1
                    aa += 1
            else:
                newdict[int(item)] = 1
        if target in newdict.keys():
            print(True)
            return True
        print(False)
        return False


numA = ['10-13', 18, '27-45', 28, '70-100', 58]
target = 98
sol = Solution()
sol.trap(nums=numA, target=target)







