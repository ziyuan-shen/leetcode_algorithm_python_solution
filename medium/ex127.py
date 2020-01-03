from collections import defaultdict
from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        if beginWord in wordList:
            wordList.remove(beginWord)
        wordlen = len(beginWord)
        predic = defaultdict(list)
        for word in wordList:
            for i in range(wordlen):
                predic[word[:i] + '*' + word[i+1:]].append(word)
        q = deque([(beginWord, 1)])
        visited = {}
        while q:
            word, level = q.popleft()
            nextwords = []
            for i in range(wordlen):
                nextwords.extend(predic[word[:i] + '*' + word[i+1:]])
            for nextword in nextwords:
                if nextword == endWord:
                    return level + 1
                if nextword not in visited:
                    visited[nextword] = True
                    q.append((nextword, level+1))
        return 0