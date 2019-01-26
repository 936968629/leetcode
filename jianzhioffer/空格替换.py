class Solution:
    """
    @param: string: An array of Char
    @param: length: The true length of the string
    @return: The true length of new string
    """

    def replaceBlank(self, string, length):
        # write your code here
        if string is None:
            return length
        count = 0
        for i in string:
            if i == " ":
                count += 1

        L = length + count * 2
        index = L - 1
        for i in range(length - 1, -1, -1):
            if string[i] == " ":
                string[index] = '0'
                string[index - 1] = '2'
                string[index - 2] = '%'
                index -= 3
            else:
                string[index] = string[i]
                index -= 1
        print(string)
        return L


sol = Solution()
res = sol.replaceBlank(" ", 1)
print(res)