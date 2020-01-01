class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.historic = {sentences[i]: times[i] for i in range(len(sentences))}
        self.inputwords = ""

    def input(self, c: str) -> List[str]:
        if c != "#":
            self.inputwords += c
            hots = []
            for sentence in self.historic:
                if sentence[:len(self.inputwords)] == self.inputwords:
                    hots.append([sentence, self.historic[sentence]])
            hots.sort(key = lambda x: (-x[1], x[0]))
            return [hot[0] for hot in hots[:min(3, len(hots))]]
        else:
            if self.inputwords in self.historic:
                self.historic[self.inputwords] += 1
            else:
                self.historic[self.inputwords] = 1
            self.inputwords = ""
            return []

# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)