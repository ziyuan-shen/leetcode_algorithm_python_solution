class Solution:
    def uniqueMorseRepresentations(self, words) -> int:
        table = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        words_coded = []
        for i in range(len(words)):
            word_coded = ''
            for j in range(len(words[i])):
                word_coded += table[ord(words[i][j])-97]
            if word_coded not in words_coded:
                words_coded.append(word_coded)
        return len(words_coded)
