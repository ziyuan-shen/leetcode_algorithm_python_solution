from collections import defaultdict
from collections import deque
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList:
            return []
        wordList.append(beginWord)
        transdic = defaultdict(set)
        for word in wordList:
            for i in range(len(word)):
                transdic[word[:i] + "*" + word[i+1:]].add(word)
        q = deque([(beginWord, 0)])
        visited = {word: False for word in wordList}
        visited[beginWord] = True
        visited_words = defaultdict(list)
        find = False
        while q and not find:
            word, level = q.popleft()
            neighbors = set()
            for i in range(len(word)):
                transword = word[:i] + "*" + word[i+1:]
                for neighbor in transdic[transword]:
                    neighbors.add(neighbor)
            for neighbor in neighbors:
                if neighbor == endWord:
                    find = True
                    break
                if not visited[neighbor]:
                    visited[neighbor] = True
                    visited_words[level+1].append(neighbor)
                    q.append((neighbor, level + 1))
        if not find:
            return []
        ans = [[endWord]]
        for l in range(level, 0, -1):
            new = []
            for seq in ans:
                last_word = seq[-1]
                neighbors = set()
                for i in range(len(last_word)):
                    transword = last_word[:i] + "*" + last_word[i+1:]
                    for neighbor in transdic[transword]:
                        neighbors.add(neighbor)
                for word in visited_words[l]:
                    if word in neighbors:
                        new.append(seq + [word])
            ans = new
        return [[beginWord] + seq[::-1] for seq in ans]