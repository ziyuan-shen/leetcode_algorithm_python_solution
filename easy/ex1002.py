class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        common_list = []
        first_word = A[0]
        A = list(map(lambda x: list(x), A))
        for char in first_word:
            flag = True
            for word in A[1:]:
                if char not in word:
                    flag = False
                    break
            if flag:
                common_list.append(char)
                for word in A:
                    word.remove(char)
        return common_list