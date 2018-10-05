class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        """
        stack = []
        for item in path:
            if item == '/':
                length = len(stack)
                if length == 0:
                    stack.append(item)
                    continue
                endItem = stack[length-1]
                if endItem == '/':
                    continue
                elif endItem == '.':
                    secondItem = stack[length-2]
                    if secondItem == '.':
                        # 倒退
                        count = 0
                        while count < 2:
                            if stack == []:
                                break
                            if stack.pop() == '/':
                                count += 1
                        stack.append('/')
                    else:
                        stack.pop()
                else:
                    stack.append(item)
            else:
                stack.append(item)
        print(stack)
        while stack[len(stack) -1] == '/' or stack[len(stack)-1] == '.':
            if len(stack) > 1 and stack[len(stack) -1] == '/':
                stack.pop()
            elif len(stack) > 1 and stack[len(stack) -1] == '.':
                
            else:
                break
        # print(stack)
        strr = ''.join(stack)
        print(strr)
        return strr
        """
        places = [p for p in path.split("/") if p != "." and p != ""]
        print(places)
        stack = []
        for p in places:
            if p == "..":
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(p)
        print(stack)
        print("/" + "/".join(stack))
        return "/" + "/".join(stack)


path = "/a/./b/../../c/"
path = "/a/../b"
# path = "/."
# path = "/..."
sol = Solution()
sol.simplifyPath(path)