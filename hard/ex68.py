class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ans = []
        while words != []:
            line = ""
            word = words.pop(0)
            line += word
            while words != []:
                word = words.pop(0)
                new_line = line + " " + word
                if len(new_line) <= maxWidth:
                    line = new_line
                else:
                    words.insert(0, word)
                    break
            if words == []:
                line = line.ljust(maxWidth)
            else:
                if len(line) < maxWidth:
                    if len(line.split(" ")) == 1:
                        line = line.ljust(maxWidth)
                    else:
                        wordList = line.split(" ")
                        word_num = len(wordList)
                        space_num = maxWidth - len(line)
                        slot_num = word_num - 1
                        quotient = space_num // slot_num
                        remainder = space_num % slot_num
                        line = ""
                        for i in range(remainder):
                            line = line + wordList[i]
                            line = line + " " * (quotient + 2)
                        for i in range(remainder, word_num - 1):
                            line = line + wordList[i]
                            line  = line + " " * (quotient + 1)
                        line += wordList[-1]
            ans.append(line)
        return ans