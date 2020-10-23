class Node:
    def __init__(self):
        self.children = dict()
        self.endWord = False

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        p = self.root
        for char in word:
            if char not in p.children:
                p.children[char] = Node()
            p = p.children[char]
        p.endWord = True
                
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        p = self.root
        for char in word:
            if char not in p.children:
                return False
            else:
                p = p.children[char]
        return p.endWord

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        p = self.root
        for char in prefix:
            if char not in p.children:
                return False
            else:
                p = p.children[char]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)