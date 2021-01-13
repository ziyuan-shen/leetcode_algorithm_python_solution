class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letterlogs = []
        digitlogs = []
        for log in logs:
            if log.split(" ")[1].isalpha():
                letterlogs.append(log)
            else:
                digitlogs.append(log)
        letterlogs.sort(key = lambda x: (" ".join(x.split(" ")[1:]), x.split(" ")[0]))
        return letterlogs + digitlogs