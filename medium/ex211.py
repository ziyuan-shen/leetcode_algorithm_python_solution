class TrieNode:
    def __init__(self):
        self.child = {}
        self.endWord = False

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = TrieNode()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        root = self.trie
        for char in word:
            if char not in root.child:
                root.child[char] = TrieNode()
            root = root.child[char]
        root.endWord = True      
        
    def searchRoot(self, word, root):
        for i, char in enumerate(word):
            if char != "." and char not in root.child:
                return False
            elif char != ".":
                root = root.child[char]
            else:
                for child_char in root.child:
                    if self.searchRoot(word[i+1:], root.child[child_char]):
                        return True
                return False
        return root.endWord

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        return self.searchRoot(word, self.trie)
        
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)