class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        if beginWord in wordList:
            wordList.remove(beginWord)
        wordList.insert(0, beginWord)
        wordlen = len(beginWord)
        edges = []
        for i in range(len(wordList)-1):
            for j in range(i+1, len(wordList)):
                if sum([wordList[i][k] == wordList[j][k] for k in range(wordlen)]) == wordlen - 1:
                    edges.append([i, j])
        visited = [[0]]
        visitedseq = [0]
        flag = True
        while len(visitedseq) < len(wordList) and flag:
            flag = False
            prevs = visited[-1]
            visited.append([])
            for prev in prevs:
                for edge in edges:
                    if edge[0] == prev and edge[1] not in visitedseq:
                        if wordList[edge[1]] == endWord:
                            return len(visited)
                        visited[-1].append(edge[1])
                        visitedseq.append(edge[1])
                        flag = True
                    if edge[1] == prev and edge[0] not in visitedseq:
                        if wordList[edge[0]] == endWord:
                            return len(visited)
                        visited[-1].append(edge[0])
                        visitedseq.append(edge[0])
                        flag = True
        return 0