class Node:
    def __init__(self, val):
        self.val = val
        self.endWord = False
        self.children = dict()

class Trie:
    def __init__(self):
        self.root = Node("")
    
    def isConcatenated(self, word):
        p = self.root
        i = 0
        while i < len(word):
            if word[i] in p.children:
                p = p.children[word[i]]
                i += 1
                if p.endWord:
                    if i == len(word):
                        return True
                    elif self.isConcatenated(word[i:]):
                        return True
            else:
                break
        return False
    
    def insert(self, word):
        p = self.root
        for letter in word:
            if letter not in p.children:
                p.children[letter] = Node(letter)
            p = p.children[letter]
        p.endWord = True
        
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        words.sort(key = lambda x: len(x))
        t = Trie()
        ans = []
        for word in words:
            if word != "":
                if t.isConcatenated(word):
                    ans.append(word)
                else:
                    t.insert(word)
        return ans