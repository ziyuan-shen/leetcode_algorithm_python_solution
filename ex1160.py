class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        length = 0
        for word in words:
            word_len = len(word)
            letters = list(chars)
            test = True
            for i in range(word_len):
                if word[i] in letters:
                    letters.remove(word[i])
                else:
                    test = False
            length += test * word_len
        return length