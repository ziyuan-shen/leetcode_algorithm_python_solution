class TrieNode:
    def __init__(self):
        self.children = {}
        self.endWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        p = self.root
        for letter in word:
            if letter not in p.children:
                p.children[letter] = TrieNode()
            p = p.children[letter]
        p.endWord = True

class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        for word in words:
            self.trie.insert(word[::-1])
        self.letters = []
        
    def query(self, letter: str) -> bool:
        self.letters.append(letter)
        p = self.trie.root
        for idx in range(len(self.letters) - 1, -1, -1):
            if self.letters[idx] in p.children:
                p = p.children[self.letters[idx]]
                if p.endWord:
                    return True
            else:
                return False
        return p.endWord
            

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)