class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        length = self.search([beginWord], endWord, wordList)
        return length if length != float("inf") else 0
    
    def search(self, sequence, endWord, wordList):
        prev = sequence[-1]
        lengths = []
        for word in wordList:
            if word not in sequence and sum([word[i] == prev[i] for i in range(len(prev))]) == len(prev) - 1:
                if word == endWord:
                    return len(sequence) + 1
                lengths.append(self.search(sequence+[word], endWord, wordList))
        if lengths == []:
            return float("inf")
        else:
            return min(lengths)

s = Solution()
print(s.ladderLength("qa", "sq", ["si","go","se","cm","so","ph","mt","db","mb","sb","kr","ln","tm","le","av","sm","ar","ci","ca","br","ti","ba","to","ra","fa","yo","ow","sn","ya","cr","po","fe","ho","ma","re","or","rn","au","ur","rh","sr","tc","lt","lo","as","fr","nb","yb","if","pb","ge","th","pm","rb","sh","co","ga","li","ha","hz","no","bi","di","hi","qa","pi","os","uh","wm","an","me","mo","na","la","st","er","sc","ne","mn","mi","am","ex","pt","io","be","fm","ta","tb","ni","mr","pa","he","lr","sq","ye"]))