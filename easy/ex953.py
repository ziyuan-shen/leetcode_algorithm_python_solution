class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dic = {letter: i for i, letter in enumerate(order)}
        def compareString(s1, s2):
            '''
            return True if s1<=s2
            '''
            l1 = len(s1)
            l2 = len(s2)
            l = min(l1, l2)
            for i in range(l):
                if dic[s1[i]] < dic[s2[i]]:
                    return True
                if dic[s1[i]] > dic[s2[i]]:
                    return False
            return l1<=l2
        for i in range(len(words) - 1):
            if not compareString(words[i], words[i+1]):
                return False
        return True