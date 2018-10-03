class Solution:
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        '''
        hash_table = {}
        list_str = str.split(' ')
        if len(pattern) != len(list_str) : return False
        #Contruct the hash_table
        for i in range(len(pattern)):
            if pattern[i] not in hash_table and list_str[i] not in hash_table.values():
                hash_table[pattern[i]] = list_str[i]
        test_str=""
        #Recreate a string from the pattern
        for char in list(pattern):
            if char not in hash_table.keys():
                return False
            test_str+=hash_table[char]
            test_str+=" "
        return str == test_str[:-1]
        '''
        strList = str.split(' ')
        dic = {}
        if len(pattern) != len(strList) or len(set(pattern)) != len(set(strList)):
            return False
        for i, v in enumerate(pattern):
            if v not in dic:
                dic[v] = strList[i]
            else:
                if dic[v] != strList[i]:
                    return False
        return True


# pattern = "abba"
# str = "dog cat cat dog4"
pattern = "abba"
str = "dog dog dog dog"
sol = Solution()
res = sol.wordPattern(pattern, str)
print(res)