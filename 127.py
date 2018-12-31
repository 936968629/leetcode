class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordList = set(wordList)
        visited = set()
        visited.add(beginWord)
        dist = 1

        while endWord not in visited:
            temp = set()
            for word in visited:
                for i in range(len(word)):
                    chars = list(word)
                    for j in range(ord('a'), ord('z') + 1):
                        chars[i] = chr(j)
                        newWord = ''.join(chars)
                        if newWord in wordList:
                            temp.add(newWord)
                            wordList.remove(newWord)

            dist += 1
            if len(temp) == 0:  # if 0, it never gets to the endWord
                return 0

            visited = temp

        return dist


beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
sol = Solution()
res = sol.ladderLength(beginWord, endWord, wordList)
print(res)
