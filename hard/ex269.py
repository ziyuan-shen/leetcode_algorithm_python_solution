class Solution:
    def getOrder(self, words):
        while words and words[0] == "":
            words.pop(0)
        if len(words) > 1:
            if words[0] == "":
                raise Exception("No answer")
            letter = words[0][0]
            subwords = [words[0][1:]]
            for word in words[1:]:
                if word == "":
                    raise Exception("No answer")
                if word[0] == letter:
                    subwords.append(word[1:])
                else:
                    self.getOrder(subwords)
                    subwords = []
                    self.graph[letter].add(word[0])
                    letter = word[0]
                    subwords.append(word[1:])
            self.getOrder(subwords)
    
    def containCircle(self, graph):
        nodes = list(graph.keys())
        def dfs(node, visited, start):
            for nei in graph[node]:
                if nei == start:
                    return True
                if nei not in visited:
                    visited.add(nei)
                    if dfs(nei, visited, start):
                        return True
            return False
        checked = set()
        for node in nodes:
            if node not in checked:
                if dfs(node, {node}, node):
                    return True
                checked.add(node)
        return False
        
    def alienOrder(self, words: List[str]) -> str:
        letters = set("".join(words))
        self.graph = {letter: set() for letter in letters}
        try:
            self.getOrder(words)
        except:
            return ""
        if self.containCircle(self.graph):
            return ""
        nodes = list(self.graph.keys())
        visited = set()
        ans = ""
        def dfs(node):
            for nei in self.graph[node]:
                if nei not in visited:
                    visited.add(nei)
                    dfs(nei)
            nonlocal ans
            ans = node + ans
        for node in nodes:
            if node not in visited:
                visited.add(node)
                dfs(node)
        return ans